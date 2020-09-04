def shell_sort(arr):

	gap = len(arr) // 2

	while gap > 0:

		for i in range(gap, len(arr)):
			temp = arr[i]
			j = i

			while j >= gap and arr[j - gap] > temp:
				arr[j] = arr[j - gap]
				j = j - gap
			arr[j] = temp

		gap = gap // 2
	return arr


arr = [19, 2, 31, 45, 30, 11, 121, 27]

print(shell_sort(arr))
