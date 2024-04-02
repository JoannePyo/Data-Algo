'''
Linked List Cycle II (Medium)

Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously 
following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer 
is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.
'''

'''
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import Optional


class Solution:
    def detectCycle(self, head):
        hashset = set()
        node = head

        while node is not None:
            if node in hashset:
                return node
            else:
                hashset.add(node)
                node = node.next

        # 순환을 감지하지 못한 경우 None을 반환합니다.
        return None 
    

'''
Time Complexity: O(n)
Space Complexity: O(n)
'''