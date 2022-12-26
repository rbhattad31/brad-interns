def SieveOfEratosthenes(num):
    prime = [True for _ in range(num + 1)]
    print(prime)
    # boolean array
    p = 2
    while p * p <= num:

        # If prime[p] is not
        # changed, then it is a prime
        if prime[p]:

            # Updating all multiples of p
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1
    print(prime)

    # Print all prime numbers
    for p in range(2, num + 1):
        if prime[p]:
            print(p)


# Driver code
if __name__ == '__main__':
    num = 50
    print("Following are the prime numbers smaller"),
    print("than or equal to", num)
    SieveOfEratosthenes(num)
