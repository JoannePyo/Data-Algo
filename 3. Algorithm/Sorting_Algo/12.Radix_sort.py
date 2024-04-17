'''
def countingSort(arr, exp):
	

def radixSort(arr):


arr = [ 170, 45, 75, 90, 802, 24, 2, 66]
radixSort(arr)
for i in range(len(arr)):
	print(arr[i],end=" ")
'''

def countingSort(arr, exp):
    size = len(arr)
    output = [0] *size
    count = [0] * 10

    for i in range(0,size):
            index= arr[i]/exp
            count[int(index)%10] += 1
            
    for i in range(1,10):
            count[i] += count[i-1]
    
    i = size-1
    while i >=0:
            index=arr[i]/exp
            output[count[int(index)%10] -1] = arr[i]
            count[int(index)%10] -= 1
            i -=1

    for i in range(0,size):
            arr[i] = output[i]

def radixSort(arr):
    max_number = max(arr)
    exp = 1
    while max_number // exp > 0:
            countingSort(arr,exp)
            exp *= 10


# Driver code to test above
arr = [ 170, 45, 75, 90, 802, 24, 2, 66]
radixSort(arr)
for i in range(len(arr)):
	print(arr[i],end=" ")
       
'''
Time complexity: O(n*d)
space complexity: O(n)
'''