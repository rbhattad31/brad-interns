def newtons_fourth(y):
    x=1
    N=0
    previous_x = None
    final = None

    while N < 50:
        x=1/4*(3*(x) + y/(x**3))
        N=N+1
        print('Iteration number:',N)
        print('Estimation:',x)
        print('Previous x:',previous_x)
        print()

        if previous_x is not None:
            if abs(x - previous_x) < 0.0001:
                final=1
                print('Difference negligible')
                print('Final Estimation:',x)
                return

    previous_x = x

    if final!=1:
        print(previous_x)