def fact(x, n):
	if x <= n:
		return x
	else:
		return x * fact(x - 1, n)
print(fact(10, 3))