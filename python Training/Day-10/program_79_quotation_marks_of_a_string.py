sentence = "pawan is 90 years old. he wants 120 coffees"
num = []
for word in sentence.split():
    if word.isdigit():
        num.append(word)
print(num)
