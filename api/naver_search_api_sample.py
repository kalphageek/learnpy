import requests
import pprint

headers = {
    'X-Naver-Client-Id': 'TVcdGN3l5f8ZIswuZ4tX',
    'X-Naver-Client-Secret': '4F9aWQDSdZ',
}

payload = {
    'query': '파이썬',
    'display': 100
}

url = 'https://openapi.naver.com/v1/search/blog'

res = requests.get(url, headers=headers, params=payload)
print('request sended..')

result = res.json()['items'][2]['title']

print(result)
