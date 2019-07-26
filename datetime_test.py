from datetime import time
from datetime import date
from datetime import datetime
#시간의 차이 다룰때 사용
from datetime import timedelta

bedtime = time(22,12,34)
print(bedtime)

theday = date(2018,12,21)
print(theday)

now = datetime.now()
#날짜 포맷
print(now.strftime('%Y/%m/%d %H:%M:%S'))

print(bedtime.hour)
print(theday.isoformat())

dday = timedelta(days=1000)
print(now + dday)

