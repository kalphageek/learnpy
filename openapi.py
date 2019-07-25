import requests
import pprint

headers = {
    'X-Naver-Client-Id': '9qTwRVUXrl6d8KE_A9bw',
    'X-Naver-Client-Secret': '4VAmjqZDkd',
}

payload = {
    'query' : '파이썬',
    'display' : 10
}

url = 'https://openapi.naver.com/v1/search/blog'

res = requests.get(url, headers=headers, params=payload)
print('requests sended...')

result = res.json()['items'][2]['title']
pprint.pprint(result)