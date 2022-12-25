import calendar
year = 2022
month = 12
print(calendar.month(year, month))


import calendar

print("The calendar of year 2022 is : ")
print(calendar.calendar(2022, 2, 1, 6))
print("The starting day number in calendar is : ", end="")
print(calendar.firstweekday())
