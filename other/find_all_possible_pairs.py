# Print all possible pairs of elements in a list

def permute(list, s):
	if list == 1:
		return s
	else:
		return [ y + x
			for y in permute(1, s)
			for x in permute(list - 1, s)
			]

# Without any permutation
print(permute(1, ['1', '2', '3']))
# With permutation
print(permute(2, ['1', '2', '3']))

