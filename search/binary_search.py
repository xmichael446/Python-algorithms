def bin_search(arr, item):
	low = 0
	high = len(arr) - 1
	while low <= high:
		mid = round((low + high) / 2)
		guess = arr[mid]
		if guess == item:
			return mid
		elif guess > item:
			high = mid - 1
		else:
			low = mid + 1
	return -1

nums = [i for i in range(21)]

guess = bin_search(nums, 13)

print(guess)