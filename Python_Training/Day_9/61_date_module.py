from datetime import date
"""
my_date=date(2023,1,6)
print("Date is " ,my_date)
"""
#for printing min_date and max_date
"""
mindate=date.min
print("Min Date is ",mindate)
maxdate=date.max
print("Max Date is" ,maxdate)
"""
#accessing year month and date
"""
my_date=date(2023,1,6)
print("Day" ,my_date.day)
print("Month" ,my_date.month)
print("Year" ,my_date.year)
"""
"""
my_date=date(2023,1,6)
Time=date.ctime(my_date)
print("Time is " ,Time)
"""
"""
today=date.today()
print("Today's date is ",today)
"""
"""
#to print weekday
today=date.today()
weekday=date.isoweekday(today)
print(weekday)
"""
#update
"""
my_date=date(2023,1,6)
my_date_update=date.replace(my_date,2022,12,24)
print(my_date_update)
"""
"""
today=date.today()
print(today.weekday())
print(today.toordinal())
print(date.timetuple(today))
"""
from datetime import time
#to print time
"""
my_time=time(12,33,36)
print(my_time)
"""
"""
my_time=time(hour=12)
print(my_time)
"""
#to print min and max time
"""
mintime=time.min
maxtime=time.max
print(mintime)
print(maxtime)
"""
#to print hour,min,sec and MS
"""
my_time=time(12,30,12,2333)
print("Hour" ,my_time.hour)
print("Min",my_time.minute)
print("Sec",my_time.second)
print("MS" ,my_time.microsecond)
"""
# format time
"""
my_time=time(16,40,12)
Ftime=my_time.strftime("%I:%M %p")
print(Ftime)
"""
from datetime import datetime
#to import both date and time simultaneously
"""
date_time=datetime(2023,1,6,12,45,23)
print(date_time)
"""
today=datetime.today()
print(today)
