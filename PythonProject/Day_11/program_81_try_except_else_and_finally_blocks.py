def divide(x, y):
    try:
        result = x // y
    except ZeroDivisionError:
        print("sorry ! you are dividing by zero")
    else:
        print("yeah! your answer is :", result)
    finally:
        print("this is always executed")

divide(4, 2)
divide(1546, 0)
divide(541, 2)