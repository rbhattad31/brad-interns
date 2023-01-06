from datetime import date
my_date=date(2020,1,6)
print("The YYYY-MM-DD format is" ,my_date)
updated=my_date.strftime("%d-%m-%Y")
print("The DD-MM-YYYY format is" ,updated)
