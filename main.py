animals = {
    'chicken': 23,
    'goat': 678,
    'pig': 1296,
    'cow': 3848,
    'sheep': 6769
}

coin = int(input())

key_list = []
value_list = []

for key, value in animals.items():
    key_list.append(key)
    value_list.append(value)


for i in value_list[::-1]:
    max_value = max(value_list)
    if coin > i:
        amount = coin // i
        if (amount > 1) and (key_list[value_list.index(i)] != 'sheep'):
            animal = f'{key_list[value_list.index(i)]}s'
        else:
            animal = key_list[value_list.index(i)]
        print(f'{amount} {animal}')
        break
    elif i == value_list[::-1][-1] and coin < i:
        print('None')

