def SieveOfEratosthenes(n):
	prime = []
	for i in range(n + 1):
		prime.append(True)
	p = 2
	while p * p <= n:
		if prime[p]:
			for i in range(p * p, n + 1, p):
				prime[i] = False
		p += 1
	for p in range(2, n + 1):
		if prime[p]:
			print(p)
if __name__ == '__main__':
	num = 100
	print("Following are the prime numbers smaller"),
	print("than or equal to", num)
	SieveOfEratosthenes(num)
