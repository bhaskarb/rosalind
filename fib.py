def fib(n, k):
	if n <= 2:
		return 1
	pop = [1]*n
	for i in range(2, n):
		pop[i] = pop[i - 1] + k*pop[i-2]
	return pop[n-1]

if __name__ == "__main__":
	print fib(34, 2)
