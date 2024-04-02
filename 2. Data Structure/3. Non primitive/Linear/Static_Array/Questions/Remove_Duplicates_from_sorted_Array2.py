'''
Remove Duplicates from Sorted Array II (Medium) 

Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element 
appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed 
in the first part of the array nums. More formally, if there are k elements after removing the duplicates, 
then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
'''

from typing import List

def removeDuplicates(self, nums: List[int]) -> int:
    empty_list = []
    for i in range(len(nums)):
        if nums[i-2] != nums[i]:
            empty_list.append(nums[i])
    return empty_list

nums = [1, 1, 1, 2, 2, 3,4,4,4,4,4,4]

result = removeDuplicates(None, nums)  # None은 클래스 메서드에서 사용되는 self 역할을 합니다
print(result)

'''
time complexity: O(n)
space complexity: O(n)
'''