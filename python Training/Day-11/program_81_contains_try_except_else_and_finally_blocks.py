try:
    x = float(input())
    ans = 10 / x
    print(ans)
    print("no exception occurred")
except Exception as e:
    print("exception occurred:", e)
else:
    print("else block is executing")
finally:
    print("executed")
