# Linear search

def linear_search(arr, item):
	for i in range(len(arr)):
		if arr[i] == item:
			return i
	return None


print(linear_search([i for i in range(10)], 2))
