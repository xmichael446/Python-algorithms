def fibonacci(n):
	a = 0
	b = 1
	arr = []
	for i in range(n):
		a, b = b, a+b
		arr.append(a)
	return arr

print(fibonacci(10))