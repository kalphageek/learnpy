import requests
import pprint

headers = {
    'X-Naver-Client-Id': '9qTwRVUXrl6d8KE_A9bw',
    'X-Naver-Client-Secret': '4VAmjqZDkd',
}

payload = {
    'query': '파이썬',
    'display': 5
}

url = 'https://openapi.naver.com/v1/search/blog'

res = requests.get(url, headers=headers, params=payload)
print('request sended..')

pprint.pprint(res.json())

result = res.json()['items'][0]['title']
print(result)
