'''
def shellSort(arr):

arr = [12, 34, 54, 2, 3]
shellSort(arr)
print("\nArray after sorting:")
for i in range(len(arr)):
    print(arr[i])
'''

def shellSort(arr):
    n = len(arr)  # 5
    gap = n // 2  # 2

    while gap > 0:              # 2
        for i in range(gap, n): # i=2 (2,5)                                             # i=3                                              # i= 4
            key = arr[i]       # key = 54                                               # key = 2
            j = i               # j = 2                                                 # j =3
            while j >= gap and arr[j - gap] > key: #2 >=2 and arr[2-2] > key -> False   # 3>=2 and arr[3-2] = arr[1] = 34 > 2  # False
                arr[j] = arr[j - gap]                                                   # arr[3] = arr[3-2]=>arr[1]=>arr[3]=34
                j -= gap                                                                # 3-=2 => j=1
            arr[j] = key                           #arr[2] = 54                                                               #arr[1] = 2
        gap //= 2

arr = [12, 34, 54, 2, 3]
shellSort(arr)
print("\nArray after sorting:")
for i in range(len(arr)):
    print(arr[i])