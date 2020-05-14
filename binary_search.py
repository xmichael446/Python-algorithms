def bin_search(arr, item):
	low = 0
	high = len(arr) - 1
	while low <= high:
		mid = round((low + high) / 2)
		guess = arr[mid]
		if guess == item:
			return mid
		elif guess > high:
			high = mid - 1
		else:
			low = mid + 1
	return None

nums = [1, 3, 5, 7, 9, 11, 13, 15]

print(bin_search(nums, 9))