'''
def insertionSort(arr):


def bucketSort(arr):


# Driver Code
arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
print("Sorted Array is")
print(bucketSort(arr))
'''
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        front = i - 1
        while front >= 0 and arr[front] > key:
            arr[front + 1] = arr[front]
            front -= 1
        arr[front + 1] = key
    return arr

def bucketSort(arr):
    bucket = []
    slot_num = 10 # 10 means 10 slots, each slot's size is 0.1
    
    # slot_number만큼의 빈 bucket 만들기
    for i in range(slot_num):
        bucket.append([])

    # Put array elements in different buckets
    # bucket들중에 안에 여러개 있는 경우 그안에서 정렬해주기.
    for j in arr:
        index = int(slot_num * j)
        bucket[index].append(j)

    # Sort individual buckets
    for i in range(slot_num):
        bucket[i] = insertionSort(bucket[i])

    # concatenate the result
    k = 0
    for i in range(slot_num):
        for j in range(len(bucket[i])):
            arr[k] = bucket[i][j]
            k += 1
    return arr

# Driver Code
arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
print("Sorted Array is")
print(bucketSort(arr[:])) 