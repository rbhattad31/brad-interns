# 1. date class
# get Today's year, month and date
from datetime import date
today = date.today()
print("current year:", today.year)
print("current year:", today.month)
print("current year:", today.day)
print("**************************************")
# Time class
from datetime import time
Time = time(11, 34, 56)
print("hour =", Time.hour)
print("minute =", Time.minute)
print("second =", Time.second)
print("microsecond =", Time.microsecond)
print("******************************************")
# date time class
from datetime import time
a = datetime(2000, 12, 12, 12, 12, 12)
print("year=", a.year)
print("month=", a.month)
print("hour=", a.hour)
print("minute=", a.minute)
print("timestamp=", a.timestamp)
print("*******************************************")
#