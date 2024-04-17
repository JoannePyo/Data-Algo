'''
def cocktail_sort(arr):

arr = [64, 34, 25, 12, 22, 11, 90]
cocktail_sort(arr)
print("정렬된 리스트:", arr)
'''
def cocktail_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n-1

    while (swapped == True):
        swapped == False
        for i in range(start, end):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True

        swapped= False
        end = end-1

        for i in range(end-1,start-1,-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
                
        start = start+1

    

# 정렬할 리스트를 생성하고 테스트
arr = [64, 34, 25, 12, 22, 11, 90]
cocktail_sort(arr)
print("정렬된 리스트:", arr)