import calendar
import datetime

x = datetime.datetime(2022, 5, 7)
print(x)

for i in range(1, 13):
    print(i, calendar.month_name[i])
    if i == 1 or i == 2 or i == 3:
        print("Q4 Fy 2022-2023")
    elif i == 4 or i == 5 or i == 6:
        print("Q1 FY 2022-2023")
    elif i == 7 or i == 8 or i == 9:
        print("Q2 FY 2022-2023")
    elif i == 10 or i == 11 or i == 12:
        print("Q3 FY 2022-2023")
