'''
import heapq
def heap_sort(arr):

# Driver Code
arr = [60, 20, 40, 70, 30, 10]
print("Sorted Array: ", heap_sort(arr))
'''
import heapq
def heap_sort(arr):
	heapq.heapify(arr)                   # [10,20,40,70,30,60]
	result = []
	while arr:                           #[10,20,40,70,30,60]   #[20,30,40,70,60] #[30,60,40,70]  #[40,60,70]
		# #가장 작은 요소가 배열에서 추출됨
		result.append(heapq.heappop(arr))  #[10]                  #[10,20]          #[10,20,30]
	return result

# Driver Code
arr = [60, 20, 40, 70, 30, 10]
print("Sorted Array: ", heap_sort(arr))