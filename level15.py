# Level 15
# http://www.pythonchallenge.com/pc/return/uzi.html


import calendar
import datetime

for year in range(1006, 1996, 10):
    d = datetime.date(year, 1, 26)
    if d.isoweekday() == 1 & calendar.isleap(year):
        print(d)

# 1756-01-27  brithday Mozart
# Next level: http://www.pythonchallenge.com/pc/return/mozart.html
