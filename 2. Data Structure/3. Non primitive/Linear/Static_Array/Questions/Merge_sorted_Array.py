'''
Merge Sorted Array(Easy)

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
'''


from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2[:n]
        return nums1.sort()


# Input lists
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

solution = Solution()
solution.merge(nums1, m, nums2, n)
print(nums1)


'''
time complexity: O((m + n) log(m + n))
space complexity: O(1)
'''

'''
Solution2

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        #Write the elements of num2 into the end of nums1
        for i in range(n):   # range(n) = 2,5,6
            nums1[m + i] = nums2[i] 
            #nums1[3+0]이니깐 nums1 index3에 다가 nums2[0]의 값인 2를 붙이는 거다.   
            # nums1 = [1,2,3,2,0,0]
            # nums1 = [1,2,3,2,5,0]
            # nums1 = [1,2,3,2,5,6]
            
        # Sort nums1 list in-place.
        nums1.sort() # [1,2,2,3,5,6]

# Input lists
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

solution = Solution()
solution.merge(nums1, m, nums2, n)
print(nums1)
'''