# Print all possible pairs of elements in a list

def permute(n, arr):
	if n == 1:
		return arr
	else:
		return [y + x for y in permute(1, arr)
										for x in permute(n - 1, arr)
										]


# Without any permutation
print(permute(1, ['1', '2', '3']))
# With permutation
print(permute(2, ['1', '2', '3']))
