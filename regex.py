import re

phone_regex = re.compile(r'((\d{2,3})[-.]?(\d{3,4}[-.]?\d{4}))')
text = 'My Number are home:031-705-4288, work:02-2324-8765'
for phone in phone_regex.findall(text):
    print('Phone No. : (' + phone[1] + ')' + phone[2] + ' => ' + phone[0])

#match()->패턴매치, search()->첫번째 반환, findall()->모두 반환, split()->, sub()->바꾸기
#r' 는 문자를 문자 자체로 인식하도록 함
#Flag -> re.I :대소문자 무시할때 사용, re.VERBOSE : 패턴이 길어지는 경우 사용-정규표현식에 주석을 달 수 있음
#r'''는 Multi Line 문자열
#(?: ... ) -> Non Capturing group
#re.match("c", "abcdef")    # No match
#re.search("c", "abcdef")   # Match
email_regex = re.compile(r'''
    ([\w\-.]+)                 #group #1 - username
    @                           #@ symbol
    ([\w\-]+(?:\.\w{2,4}){1,2})    #domain name
    ''', re.VERBOSE|re.I)     # 다중 Flags 적용
result = email_regex.search('My Email is kalphageek-01@outlook.co.kr.kr')
print('Email : '+result.group(0))
print('Username : '+result.group(1))
print('Domain : '+result.group(2))

text = """Ross McFluff: 834.345.1254 155 Elm Street
...
... Ronald Heathmore: 892.345.3428 436 Finley Avenue
... Frank Burger: 925.541.7625 662 South Dogwood Way
...
...
... Heather Albrecht: 548.326.4584 919 Park Place"""
entries = re.split("\n+", text)
for entry in entries:
    items = re.split(":? ", entry)
    for item in items:
        print(item)

#[ ] 대괄호:여러 문자 중 하나와 일치
matchObj = re.fullmatch("You[;']re studying re module[.,]", \
                        'You\'re studying re module.')
print(matchObj)