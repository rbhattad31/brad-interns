import time
from datetime import date

# initializing constructor
# and passing arguments in the
# format year, month, date

my_date = date(1996, 12, 11)
print("Date passed as argument is",my_date )
print()

# Python program to
# print current date

# calling the today
# function of date class

today = date.today()

print("Today's date is", today)
print()

# date object of today's date

today = date.today()

print("Current year:", today.year)

print("Current month:", today.month)

print("Current day:", today.day)
print()
# get date from timestamp
# Getting Datetime from timestamp

# date_time = datetime.fromtimestamp(1887639468)
#
# print("Datetime from timestamp:", date_time)
# print()

# Convert Date to String


# calling the today
# function of date class
today = date.today()

# Converting the date to the string
Str = date.isoformat(today)
print("String Representation", Str)
print(type(Str))
print()


# gives local time
a = time.localtime()
c = time.asctime(a)
print(c)
print()
print(time.ctime(1615799665.584516))
print(time.ctime(1000))
print()


# Getting a tuple of ISO Year,
# ISO Week Number and ISO Weekday

# Calling the today() function
# to return todays date
Todays_date = date.today()

# Printing today's date
print(Todays_date)

# Calling the isocalendar() function
# over the above today's date to return
# its ISO Year, ISO Week Number
# and ISO Weekday
print(Todays_date.isocalendar())
print()









