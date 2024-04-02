'''
Remove Duplicates from Sorted Array (Easy)
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place 
such that each unique element appears only once. The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
* Change the array nums such that the first k elements of nums contain the unique elements in the order they were present 
in nums initially. The remaining elements of nums are not important as well as the size of nums.
* Return k.

Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
'''

from typing import List

def removeDuplicates(self, nums: List[int]) -> int:
    empty_list = []
    for i in range(len(nums)):
        if nums[i-1] != nums[i]:
            empty_list.append(nums[i])
    return empty_list


nums = [0,0,1,1,1,2,2,3,3,4]

result = removeDuplicates(None, nums)  # None은 클래스 메서드에서 사용되는 self 역할을 합니다
print(result)


'''
time complexity: O(n)
space complexity: O(n)
'''