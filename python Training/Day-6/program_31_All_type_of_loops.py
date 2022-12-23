# for loop
values = range(5)
print(type(values))
print(list(values))
for i in values:
    print(i)
print("*********************")
# while loop
i = 1
while i < 6:
    print(i)
    i += 1
print("****************")
# break in while
i = 1
while i < 100:
    print(i)
    if i == 7:
        break
    i += 1
print("***********")
# break in 'for'
for i in range(5):
    if i == 3:
        break
    print(i)
print("***********")
# continue in while
# printing odd numbers from 1 to 10
num = 0
while num < 10:
    num += 1
    if (num % 2) == 0:
        continue
    print(num)
print("*************")
# continue in for
for i in range(5):
    if i == 3:
        continue
    print(i)
print("******************")
# pass
s = "venkat"
for i in s:
    if i == 'k':
        print('pass executed')
        pass
    print(i)
print("**********")
# do while
i = 1
while True:
    print(i)
    i = i+1
    if i > 5:
        break
