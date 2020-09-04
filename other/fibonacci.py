def fibonacci(n):
	a = b = 1
	arr = [0]
	for i in range(n):
		a, b = b, a + b
		arr.append(a)
	return arr


print(fibonacci(10))
