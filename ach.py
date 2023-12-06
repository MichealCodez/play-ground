import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import json
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

import logging

logging.basicConfig(level=logging.INFO)
es_client = Elasticsearch()


URL = os.getenv("URL") or "https://lists.linuxfoundation.org/pipermail/bitcoin-dev/"
NAME = os.getenv("NAME") or "bitcoin"

if URL == "https://lists.linuxfoundation.org/pipermail/bitcoin-dev/":
    NAME = "bitcoin"
elif URL == 'https://lists.linuxfoundation.org/pipermail/lightning-dev/':
    NAME = "lightning"

print(f"NAME: {NAME}\nURL: {URL}")

MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]

days = int(os.getenv("DAYS_TO_SUBTRACT")) or 15
start_date = datetime.now() - timedelta(days=days)

year = start_date.year
month = start_date.month - 1  # Months are 0-based in Python

DATA_DIR = os.getenv("DATA_DIR", ".")


def create_batches(elements, batch_size):
    return [elements[i:i + batch_size] for i in range(0, len(elements), batch_size)]


def download_dumps(year=year, month=month):
    if not os.path.exists(os.path.join(DATA_DIR, "mailing-list")):
        os.makedirs(os.path.join(DATA_DIR, "mailing-list"), exist_ok=True)

    consecutive_errors = 0
    while True:
        logging.info(f"Downloading {year}-{MONTHS[month]}...")
        url = URL + f"{year}-{MONTHS[month]}/date.html"
        response = requests.get(url)
        text = response.text
        soup = BeautifulSoup(text, 'html.parser')

        uls = soup.find_all('ul')
        if len(uls) == 0:
            logging.info("No more data")
            consecutive_errors += 1
            if consecutive_errors >= 6:
                break

            month += 1
            if month >= len(MONTHS):
                month = 0
                year += 1
            continue

        ul = uls[1]

        links = ul.find_all('li a')
        batches = create_batches(links, 30)

        for batch in batches:
            for link in batch:
                href = link.get('href')
                if not href:
                    continue

                file_name = os.path.join(
                    DATA_DIR, "mailing-list", f"{year}-{MONTHS[month]}-{href}"
                )
                if os.path.exists(file_name):
                    logging.info(f"Skipping {file_name}")
                    continue

                u = URL + f"{year}-{MONTHS[month]}/{href}"
                logging.info(f"Downloading {u}")
                response = requests.get(u)
                text = response.text

                with open(file_name, 'w', encoding='utf-8') as file:
                    file.write(text)

        month += 1
        if month >= len(MONTHS):
            month = 0
            year += 1


def parse_dumps():
    documents = []
    files = os.listdir(os.path.join(DATA_DIR, "mailing-list"))
    threads = {}

    for file in files:
        with open(os.path.join(DATA_DIR, "mailing-list", file), 'r', encoding='utf-8') as file:
            text = file.read()

        logging.info(f"Parsing {file}...")
        soup = BeautifulSoup(text, 'html.parser')

        author = soup.find('b').get_text() if soup.find('b') else ''
        title = (
            soup.find('h1').get_text()
            .replace("[Bitcoin-development] ", "")
            .replace("[bitcoin-dev] ", "")
            .replace("[Lightning-dev]", "")
            .replace("[lightning-dev] ", "")
            .replace("\t", " ")
            .strip()
        )
        body = soup.find('pre').get_text() if soup.find('pre') else ''
        date = datetime.strptime(soup.find('i').get_text().replace("  ", " "), "%a %b %d %H:%M:%S %Y")

        # remove any html in body
        body_text = ''.join(soup.find('pre', {'class': None}).findAll(text=True))

        file_date = f"{file.split('-')[0]}-{file.split('-')[1]}"
        file_name = file.split('-')[2]

        document = {
            'id': f"mailing-list-{NAME}-{file.replace('.html', '')}",
            'authors': [author],
            'title': title,
            'body': body_text,
            'body_type': 'raw',
            'created_at': date,
            'domain': URL,
            'url': f"{URL}{file_date}/{file_name}",
        }

        if document['title'] not in threads:
            threads[document['title']] = {
                'id': document['id'],
                'url': document['url'],
            }

        if threads[document['title']]['id'] == document['id']:
            document['type'] = 'original_post'
        else:
            document['type'] = 'reply'
            document['thread_url'] = threads[document['title']]['url']

        documents.append(document)

    return documents


def find_earliest_timestamp(documents, title):
    earliest = min(
        (d['created_at'] for d in documents if d['title'] == title),
        default=None
    )
    return earliest

def main():
    download_dumps()

    if not os.path.exists(os.path.join(DATA_DIR, "mailing-list")):
        logging.error("Please download the data first")
        exit(1)

    parsed_dumps = parse_dumps()
    with open(os.path.join(DATA_DIR, "mailing-list", "documents.json"), 'w', encoding='utf-8') as file:
        json.dump(parsed_dumps, file)

    if os.path.exists(os.path.join(DATA_DIR, "mailing-list", "documents.json")):
        with open(os.path.join(DATA_DIR, "mailing-list", "documents.json"), 'r', encoding='utf-8') as file:
            documents = json.load(file)

    logging.info(f"Found {len(documents)} documents")
    count = 0

    logging.info(f"Filtering existing {len(documents)} documents... please wait...")
    for document in documents:
        is_exist = es_client.exists(document['id'])
        if not is_exist:
            count += 1
            es_client.index(document)

    logging.info(f"Inserted {count} new documents")

if __name__ == "__main__":
    main()
