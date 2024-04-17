'''
한번 끝까지 보고 작은수부터 옮기기
def selectionSort(array, size):                


arr = [-1,15,7,2,-5,10]
size = len(arr)            
selectionSort(arr, size)
print(arr)
'''
def selectionSort(array, size):                
    for i in range(size):       #i=0 in range(6)                                                 # i=1
        min_index = i           # -1 이 min_index
        for j in range(i + 1, size):    # 1 (15, 6)   # 2 (7, 6)  # 3 (2, 6)  # 4 (-5, 6)  # 5 (10, 6)
            # select the minimum element in every iteration
            if array[min_index] > array[j]: # 15 < -1  # 7 < -1    # 2 < -1    # -5 < -1    # 10 < -1
                min_index = j                                                  # min_index = -5
        # swapping the elements to sort the array
        array[i], array[min_index] = array[min_index], array[i]                #(-1,-5) = (-5,-1)
                                                                               #[-5,15,7,2,-1,10]
arr = [-1,15,7,2,-5,10]
size = len(arr)             # def selectionSort(array): 하고 이 함수 안에 써도 된다. 그럼 selectionSort(array)가 됨.
selectionSort(arr, size)
print(arr)

'''
Time complexity: O(n*n)
Space complexity: O(1)
'''
