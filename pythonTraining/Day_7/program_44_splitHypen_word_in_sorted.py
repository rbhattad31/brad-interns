print("Enter words separated by Hyphens : ")
my_input = input().split("-")
print(my_input)
listt = [wrd for wrd in my_input]
print(listt)
listt.sort()
print(listt)
print('-'.join(listt))
