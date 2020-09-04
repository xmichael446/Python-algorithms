# Insertion sort

def insertion_sort(arr):
	for i in range(0, len(arr)):
		for j in range(i - 1, -1, -1):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
			else:
				break
	return arr


print(insertion_sort([6, 2, 3, 8, 5, 1, 7, 4]))
