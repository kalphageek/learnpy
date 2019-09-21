import csv
import pprint
import re

with open('parks.csv', 'r') as file:
    reader = csv.reader(file)
    park_list = list(reader)
ss = set()

regex = re.compile(r'[A-Z]{2}')
for items in park_list:
    for item in items:
        v = regex.match(item)
        if v is not None:
            ss.add(v.group())

for s in ss:
    pprint.pprint(s)