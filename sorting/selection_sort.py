def find_smallest(arr):
	smallest = arr[0]
	index = 0
	for i in range(len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			index = i
	return index

def s_sort(arr):
	new_arr = []
	for i in range(len(arr)):
		smallest = find_smallest(arr)
		new_arr.append(arr.pop(smallest))
	return new_arr
print(s_sort([2, 7, 1, 3, 6, 9, 4]))