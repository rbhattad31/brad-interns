import datetime

today = datetime.datetime.today()
print("today", today)
yesterday = today - datetime.timedelta(days=1)
print("yesterday:", yesterday)
Tomorrow = today + datetime.timedelta(days=1)
print("Tomorrow:", Tomorrow)
d = today + datetime.timedelta(days=5)
print("After 5 days from today:", d)
print("="*20)
x = datetime.datetime.today()
print(x)
print("="*20)
y = datetime.datetime(2019, 7, 23)
print(y)
print(y.strftime("%w"))
print("="*20)
print(y.strftime("%A"))
print("="*20)
print(y.strftime("%d"))
print("="*20)
print(y.strftime("%w"))
print("="*20)
print(datetime.datetime.today)

