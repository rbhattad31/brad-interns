def recursum(n):
    if n <= 1:
        return n
    return n + recursum(n - 1)


n = 5
print(recursum(n))
