'''
import random

def bogo_sort(arr):


to_sort = [5, 1, 12]
print(bogo_sort(to_sort))
'''
import random

def bogo_sort(arr):
    def is_sorted(arr):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]: # 현재 요소가 다음 요소보다 크다면
                return False        # (더 큰 숫자라면) False를 반환. 배열이 정렬되지 않았음. #while not is_sorted(arr)로 가기
        return True                 # 배열됨. goto return arr. 
    
    while not is_sorted(arr): 
        random.shuffle(arr)  # 배열을 무작위로 섞음. 다시 is_sorted(arr)로 가서 확인.

    return arr  # 정렬된 배열을 반환

to_sort = [5, 1, 12]
print(bogo_sort(to_sort))