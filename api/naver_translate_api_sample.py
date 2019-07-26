from requests import Request
from requests import Session

s = Session()

headers = {
    'X-Naver-Client-Id': '9qTwRVUXrl6d8KE_A9bw',
    'X-Naver-Client-Secret': '4VAmjqZDkd',
}

text = "All Python releases are Open Source. Historically, most, but not all, Python releases have also been GPL-compatible. The Licenses page details GPL-compatibility and Terms and Conditions. "

payload = {
    'source': 'en',
    'target': 'ko',
    'text': text
}

url = 'https://openapi.naver.com/v1/papago/n2mt'

req = Request('POST', url, data=payload, headers=headers)
prepped = req.prepare()

res = s.send(prepped)

result = res.json()['message']['result']['translatedText']

print(result)
