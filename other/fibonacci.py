def fib(n):
	a = b = 1
	arr = []
	for i in range(n):
		a, b = b, a+b
		arr.append(a)
	return arr

print(fib(10))
