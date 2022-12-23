import datetime

print("="*20)
x = datetime.datetime.now()
print(x)
print("="*20)
y = datetime.datetime(2019, 7, 23)
print(y.strftime("%B"))
print("="*20)
print(y.strftime("%A"))
print("="*20)
print(y.strftime("%d"))
print("="*20)
print(y.strftime("%w"))
print("="*20)


