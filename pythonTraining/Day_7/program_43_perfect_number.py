def perfect_number(n):
    sum_of = 0
    for x in range(1, n):
        if n % x == 0:
            sum_of += x
    return sum_of == n


print(perfect_number(6))
