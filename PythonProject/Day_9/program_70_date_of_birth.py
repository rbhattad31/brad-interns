import datetime


def findAge(current_date, current_month, current_year,
            birth_date, birth_month, birth_year):
    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if birth_date > current_date:
        current_month = current_month - 1
        current_date = current_date + month[birth_month - 1]

    if birth_month > current_month:
        current_year = current_year - 1
        current_month = current_month + 12
    calculated_date = current_date - birth_date
    calculated_month = current_month - birth_month
    calculated_year = current_year - birth_year
    print()
    "Present Age"
    print(calculated_year, "Years,", calculated_month, "Months,", calculated_date, "Days.")



current_time = datetime.datetime.now()
current_date = current_time.day
current_month = current_time.month
current_year = current_time.year
birth_date = int(input("enter date in your date of birth: "))
birth_month = int(input("enter month in your date of birth: "))
birth_year = int(input("enter year in your date of birth: "))

findAge(current_date, current_month, current_year,
        birth_date, birth_month, birth_year)
