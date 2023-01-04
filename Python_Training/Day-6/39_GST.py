a=int(input("Enter the price of the item"))
g=float(input("Enter GST Rate"))

if(g==5):
    res=a+(0.05*a)
    print("Final Price is %.2f" %res)

elif(g==12):
    res=a+(0.05*a)
    print("Final Price is %.2f" % res)

elif(g==18):
    res=a+(0.18*a)
    print("Final Price is %.2f" % res)

elif(g==28):
    res=a+(0.28*a)
    print("Final Price is %.2f" % res)

else:
    print("Invalid Tax Rate")