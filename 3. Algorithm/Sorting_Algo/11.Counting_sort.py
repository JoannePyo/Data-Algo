'''
def countingSort(arr):


data = [4, 2, 2, 8, 3, 3, 1]
countingSort(data)
print("Sorted Array in Ascending Order: ")
print(data)
'''
def countingSort(arr):
    size = len(arr)
    output = [0] * size

    # Initialize count array
    count = [0] * 10

    # Store the count of each elements in count array
    # 숫자 세기
    for i in range(0, size):
        count[arr[i]] += 1

    # 앞에 수랑 더하기. Store the cummulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # 자기자리 찾아가기. Find the index of each element of the original array in count array place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        arr[i] = output[i]


data = [4, 2, 2, 8, 3, 3, 1]
countingSort(data)
print("Sorted Array in Ascending Order: ")
print(data)