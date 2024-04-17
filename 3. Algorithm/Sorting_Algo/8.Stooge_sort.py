'''
2/3
def stoogesort(arr, left, right):

arr = [2, 4, 5, 3, 1]
n = len(arr)
stoogesort(arr, 0, n-1)
for i in range(0, n):
    print(arr[i], end=' ')
'''

def stoogesort(arr, left, right):
	if left >= right:
		return
	# If first element is smaller than last, swap them
	if arr[left]>arr[right]:
		arr[left], arr[right] = arr[right], arr[left]

	# If there are more than 2 elements in the array
	if right-left + 1 > 2:
		key = int((right - left + 1) / 3)
		
		# Recursively sort first 2 / 3 elements
		stoogesort(arr, left, right - key)
		
		# Recursively sort last 2 / 3 elements
		stoogesort(arr, left + key, right)
		
		# Recursively sort first 2 / 3 elements again to confirm
		stoogesort(arr, left, right - key)

# deriver
arr = [2, 4, 5, 3, 1]
n = len(arr)
stoogesort(arr, 0, n-1)
for i in range(0, n):
    print(arr[i], end=' ')