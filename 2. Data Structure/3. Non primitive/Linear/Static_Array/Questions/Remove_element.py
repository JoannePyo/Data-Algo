'''
Remove Element (Easy)
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, 
you need to do the following things:
* Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
The remaining elements of nums are not important as well as the size of nums. 
* Return k.

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
'''

from typing import List

def removeElement(nums: List[int], val: int) -> int:
    empty_list = []
    for i in range(len(nums)):
        if nums[i] != val:
            empty_list.append(nums[i])
    return empty_list


nums = [3, 2, 2, 3]
val = 3

k = removeElement(nums, val) 
print(k) 


'''
time complexity: O(n)
space complexity: O(n)
'''