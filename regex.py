import re

phone_regex = re.compile(r'((\d{2,3})[-.]?(\d{3,4}[-.]?\d{4}))')
text = 'My Number are home:031-705-4288, work:02-2324-8765'
for phone in phone_regex.findall(text):
    print('Phone No. : (' + phone[1] + ')' + phone[2] + ' => ' + phone[0])

#search()->첫번째 반환, findall()->모두 반환, split(), sub()->바꾸기
#r' 는 문자를 문자 자체로 인식하도록 함
#Flag -> re.I :대소문자 무시할때 사용, re.VERBOSE : 패턴이 길어지는 경우 사용
#r'''는 Multi Line 문자열
email_regex = re.compile(r'''
    ([\w\-.]+)                 #group #1 - username
    @                           #@ symbol
<<<<<<< HEAD
    ([\w\-]+(?:\.\w{2,4}){1,2})    #domain name
    ''', re.VERBOSE)
result = email_regex.search('My Email is kalphageek-01@outlook.co.kr.kr')
=======
    ([\w\-.]+\.\w{2,4}){1,2}    #domain name
    ''', re.VERBOSE)
result = email_regex.search('My Email is kalphageek-01@outlook.com')
>>>>>>> af4f4028bddd566ce8675a831732f64731a4d3a2
print('Email : '+result.group(0))
print('Username : '+result.group(1))
print('Domain : '+result.group(2))
