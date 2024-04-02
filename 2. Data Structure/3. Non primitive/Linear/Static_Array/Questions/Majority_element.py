'''
Majority Element(Easy)

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋times. 
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3
'''

import collections

def majorityElement(self, nums):
    hashmap = collections.Counter(nums)
    return max(hashmap.keys(), key=hashmap.get)
    
nums = [3,2,3]
result = majorityElement(None, nums)
print(result)