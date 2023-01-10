try:
    a = int(input("Enter a number"))
    assert a%2==0
except:
    print("It is not an even number")
else:
    print("a is even")
finally:
    print("The code is executed")

    