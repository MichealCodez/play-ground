from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import pyautogui as py
import requests
import os
import time

# BASE_DIR = os.path.dirname(os.path.realpath(__file__))

# captcha

#def captcha():
delay_time = 2
audio_to_text_delay = 10
website = 'https://visa.vfsglobal.com/ind/en/ita/login'
# text_to_speach = 'https://speech-to-text-demo.ng.bluemix.net'
option = webdriver.ChromeOptions()
option.add_argument('--disable-notifications')
option.add_argument("--mute-audio")
option.add_argument("user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 "
                    "(KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1")

driver = webdriver.Chrome(options=option)


def audio_to_text(path):
    driver.execute_script('''window.open("","_blank");''')
    driver.switch_to.window(driver.window_handles[1])
    driver.get("https://speech-to-text-demo.ng.bluemix.net")
    time.sleep(3)
    # root = browser.find_element(By.ID, 'root').find_elements_by_class_name('dropzone _container '
    #                                                                        '_container_large')
    btn = driver.find_element(By.XPATH, '//*[@id="root"]/div/input')
    btn.send_keys(f'{BASE_DIR}/{path}')
    # Audio to text is processing
    time.sleep(5)
    text = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[7]/div/div/div/span').text
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    return text


def save_file(content, filename):
    with open(filename, "wb") as handle:
        for data in content.iter_content():
            handle.write(data)


driver.get(website)
driver.maximize_window()
time.sleep(5)

driver.find_element(By.ID, 'mat-input-0').send_keys('zooyouyes@merry.pink')
driver.find_element(By.ID, 'mat-input-1').send_keys('@Waheguruji11')

driver.find_element(By.XPATH, '//*[@id="onetrust-close-btn-container"]/button').click()

# recaptcha = driver.find_element(By.XPATH, '/html/body/app-root/div/app-login/section/div/div/mat-card/form/'
#                                           'app-captcha-container')
#
# time.sleep(2)
# recaptcha_click = recaptcha.find_element(By.TAG_NAME, 'iframe')
# time.sleep(1)
# recaptcha_click.click()
# time.sleep(2)
# all_iframes_len = driver.find_elements(By.TAG_NAME, 'iframe')
# time.sleep(1)
# audio_btn_found = False
# audio_btn_index = -1
# for index in range(len(all_iframes_len)):
#     driver.switch_to.default_content()
#     iframe = driver.find_elements(By.TAG_NAME, 'iframe')[index]
#     driver.switch_to.frame(iframe)
#     driver.implicitly_wait(delay_time)
#     try:
#         audio_btn = driver.find_element(By.ID, 'recaptcha-audio-button') or \
#                    driver.find_element(By.ID, 'recaptcha-anchor')
#         audio_btn.click()
#         audio_btn_found = True
#         audio_btn_index = index
#         break
#     except Exception as e:
#         pass
# if audio_btn_found:
#     try:
#         href = driver.find_element(By.ID, 'audio-source').get_attribute('src')
#         audio_file = requests.get(href, stream=True)
#         save_file(audio_file, "audio.mp3")
#         audio_text = audio_to_text("audio.mp3")
#         driver.switch_to.default_content()
#         iframe = driver.find_elements(By.TAG_NAME, 'iframe')[audio_btn_index]
#         driver.switch_to.frame(iframe)
#         respond = driver.find_element(By.ID, 'audio-response')
#         respond.send_keys(audio_text)
#         respond.send_keys(Keys.ENTER)
#     except:
#         pass

time.sleep(3)

py.press('tab')
py.press('tab')
py.press('tab')
py.press('enter')

time.sleep(10)

# driver.find_element(By.ID, 'mat-checkbox-1').click()
# driver.find_element(By.ID, 'mat-checkbox-2').click()

py.press('tab')
py.press('tab')
# py.press('tab')
py.press('space')
py.press('tab')
py.press('space')

time.sleep(5)

py.press('tab')
py.press('tab')
py.press('tab')
py.press('tab')
py.press('tab')
py.press('tab')
py.press('tab')
py.press('enter')
# driver.find_element(By.XPATH, '/html/body/app-root/div/app-dashboard/section[1]/div/div[2]/button').click()

time.sleep(3)

driver.find_element(By.ID, 'mat-checkbox-3').click()

time.sleep(2)

driver.find_element(By.XPATH, '/html/body/app-root/div/app-dashboard/section/div/button').click()

time.sleep(5)

driver.find_element(By.ID, 'mat-input-2').send_keys('Faizan')
driver.find_element(By.ID, 'mat-input-3').send_keys('Yousra')
driver.find_element(By.ID, 'mat-select-0').click()
driver.find_element(By.XPATH, '//*[@id="onetrust-consent-sdk"]').click()





# driver = webdriver.Chrome()
#
# driver.get('https://visa.vfsglobal.com/tur/en/pol/login')

# driver.find_element(By.ID, 'mat-input-0').send_keys('zooyouyes@merry.pink')
# driver.find_element(By.ID, 'mat-input-1').send_keys('@Waheguruji11')


