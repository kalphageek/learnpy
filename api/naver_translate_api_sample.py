from requests import Request
from requests import Session

s = Session()

headers = {
    'X-Naver-Client-Id': 'TVcdGN3l5f8ZIswuZ4tX',
    'X-Naver-Client-Secret': '4F9aWQDSdZ',
}

text = "Yesterday all my troubles seemed so far away."

payload = {
    'source': 'en',
    'target': 'ko',
    'text': text,
}

url = 'https://openapi.naver.com/v1/language/translate'

req = Request('POST', url, data=payload, headers=headers)
prepped = req.prepare()

res = s.send(prepped)

result = res.json()['message']['result']['translatedText']

print(result)
