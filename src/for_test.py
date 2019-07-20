colors = ['red', 'yellow', 'blue', 'green', 'orange']

# for item in colors:
#     print(item)


wish_travel_city = {
    'bangkok': 'Thai',
    'LA': 'USA',
    'manila': 'Philippines'
}

# for key, value in wish_travel_city.items():
#     print(key + ': ' + value)

addresses = {
    '1': {'name': 'hong kildong', 'email': 'hong@mail.com', 'hp_num': '010-222-3333'},
    '2': {'name': 'lee soonsin', 'email': 'lee@mail.com', 'hp_num': '010-222-3333'},
    '3': {'name': 'jang youngsil', 'email': 'jang@mail.com', 'hp_num': '010-222-3333'},
    '4': {'name': 'king sejong', 'email': 'king@mail.com', 'hp_num': '010-222-3333'},
}

for key in addresses:
    my_dict = addresses[key]
    print(my_dict)

# random module
import random

for i in range(10):
    print(random.randint(1, 6))

