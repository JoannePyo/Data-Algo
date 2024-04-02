'''
[912. Sort an Array]
Given an array of integers `nums`, sort the array in ascending order and return it.
You must solve the problem without using any built-in functions in `O(nlog(n))`time 
complexity and with the smallest space complexity possible.

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), 
while the positions of other numbers are changed (for example, 1 and 5).
'''

from typing import List

class Sorting:
    def sortArray(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1, 0, -1):
            for j in range(i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

nums = [5, 2, 3, 1]
sorter = Sorting()
sorted_nums = sorter.sortArray(nums)
print(sorted_nums)
