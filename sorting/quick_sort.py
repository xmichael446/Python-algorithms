def q_sort(arr):
	if len(arr) < 2:
		return arr
	else:
		mid = round(len(arr) / 2)
		pivot = arr[mid]
		low = [i for i in arr if i < pivot]
		high = [i for i in arr if i > pivot]
		return q_sort(low) + [pivot] + q_sort(high)

my_list = [6, 2, 4, 9, 10, 1, 3, 12]
print(q_sort(my_list))