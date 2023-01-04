def myfunc(*sentence):
    for x in sentence:
        print(x,end="-")
    print()
    res=list(sentence)
    res.sort()
    for y in res:
        print(y,end="-")
myfunc('green','red','yellow','black','white')
