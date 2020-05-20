# Find minimal and maximal differences of values in an list

arr = [2, 9, 13, 71, 32]
diffs = []

for i in arr:
	for j in arr:
		if i > j:
			diffs.append(i - j)
		elif j > i:
			diffs.append(j - i)
		else:
			continue

minimal = min(diffs)
maximal = max(diffs)

print("Minimal: {} \nMaximal: {}".format(minimal, maximal))

# Output:
# Minimal: 4
# Maximal: 69