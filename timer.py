import datetime
from datetime import time
from datetime import date

now = datetime.datetime.now()
now.strftime("%Y-%m-%d %H:%M:%s")

white = date(1970,3,14)
white.month
white.day
white.year
white.isoformat()

bedtime = time(20,12,13)
bedtime.isoformat()

for i in range(30):
    time.sleep(1)
    print(i)