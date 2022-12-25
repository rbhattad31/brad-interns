import datetime
a = datetime.datetime.now()
print(a)  #print out the year month date and hours minutes seconds milliseconds
print("----------------")
print(a.year)  #printout the present year
print(a.strftime("%A"))  # printout the present day full version
print("----------------")
print(a.strftime("%Y"))  # printout the present year
print("----------------")
print(a.strftime("%m"))  # printout the present month
print("----------------")
print(a.strftime("%a"))  # 	Weekday, short version
print("----------------")
print(a.strftime("%w"))  # Weekday as a number 0-6, 0 is Sunday
print("----------------")
print(a.strftime("%d"))  # day of month
print("----------------")
print(a.strftime("%b"))  # month short name
print("----------------")
print(a.strftime("%B"))  # month full name
print("----------------")
print(a.strftime("%M"))  # month as a number
print("----------------")
print(a.strftime("%y"))  #  year short version without century
print("----------------")
print(a.strftime("%Y"))  #  year full version
print("----------------")
print(a.strftime("%H"))  # hours 00-23
print("----------------")
print(a.strftime("%I"))  #hours 00-12
print("----------------")
