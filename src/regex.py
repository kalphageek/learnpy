import re

webaddr_regex = re.compile(r'(\d{2,3})[-.]?(\d{3,4}[-.]?\d{4})')
result = webaddr_regex.search('My Number are home:031-705-4288, work:02-2324-8765')
print('Phone No. :'+result.group())
print('Phone No. :'+result.group(0))
print('Area No. :'+result.group(1))
print('Main No. :'+result.group(2))
area, main = result.groups()#tuple unpacking
print(area, main)


result = webaddr_regex.findall('My Number are home:031-705-4288, work:02-2324-8765') #-> list > tuple

#search()->첫번째 반환, findall()->모두 반환, split(), sub()->바꾸기
#r' 는 문자를 문자 자체로 인식하도록 함
#Flag -> re.I :대소문자 무시할때 사용, re.VERBOSE : 패턴이 길어지는 경우 사용
#r'''는 Multi Line 문자열
email_regex = re.compile(r'''(
    ([\w\-.+]+)                  #group #1 - username
    @                           #@ symbol
    [\w\-.]+(\.\w{2,4}){1,2}    #domain name
    )''', re.VERBOSE)
result = email_regex.search('My Email is kalphageek-01@outlook.com')
print('Email : '+result.group())
print('Username : '+result.group(1))
print('Domain : '+result.group(2))