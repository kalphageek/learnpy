import re

# search() 함수
phonenum_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phonenum_regex.search('My number is 415-555-4242.')
mo.group()


# group() 함수
phonenum_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phonenum_regex.search('My number is 415-555-4242.')


# findall() 함수
mo = phonenum_regex.search('Cell: 415-555-9999 Work: 212-555-0000')
mo.group()

finds = phonenum_regex.findall('Cell: 415-555-9999 Work: 212-555-0000')


phonenum_regex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')  # has groups
phonenum_regex.findall('Cell: 415-555-9999 Work: 212-555-0000')
# [('415', '555', '9999'), ('212', '555', '0000')]


