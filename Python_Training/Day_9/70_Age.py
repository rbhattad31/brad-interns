from datetime import date
year=int(input("Enter the year"))
month=int(input("Enter month"))
day=int(input("Enter day"))
my_date=date(year,month,day)
today=date.today()
age=today.year-my_date.year
if(my_date.month>today.month):
    age=age-1
    print(age)
elif(my_date.month==today.month):
    if(today.day<my_date.day):
        age=age-1
        print(age)
    else:
        print(age)

else:
    print(age)