import math as mt
N = 100005
def AMICABLE():
    Sum = [0 for i in range(N)]
    for i in range(1, N):
        Sum[i] += 1
        for j in range(2, mt.ceil(mt.sqrt(i))):
            if i % j == 0:
                Sum[i] += j
                if i // j != j:
                    Sum[i] += i // j
    s = set()
    for i in range(2, N):
        if (i != Sum[i] and Sum[i] < N and
                i == Sum[Sum[i]] and i not in s and
                Sum[i] not in s):
            s.add(i)
            s.add(Sum[i])
    return s
def SumOfAmicable(n):
    Sum = 0
    s = AMICABLE()
    s = sorted(s)
    for i in s:
        if i <= n:
            Sum += i
        else:
            break
    return Sum
n = 284
print(SumOfAmicable(n))
