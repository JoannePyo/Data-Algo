'''
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

'''
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
'''

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def array_to_linked_list(self, arr):
        dummy = ListNode()
        current = dummy
        for num in arr:
            current.next = ListNode(num)
            current = current.next
        return dummy.next

    def linked_list_to_array(self, head):
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return arr

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()   #Creates a completely blank ListNode
        prev = dummy     # current pointer points first node
        carry = 0           # carry는 나중에 반올림 되는 수

        while l1 or l2 :   # while l1 or l2 are null, add them together 
            L1_val = l1.val if l1 else 0  # only if l1 is not null l1, else l1 is null, setup to 0.
            L2_val = l2.val if l2 else 0

            # new digit
            val = L1_val + L2_val + carry  # 2+5=7      #4+6=10       #3+4+1(carry)=8

            # 만약 숫자가 15면 5나오고. 다음 노드에 1. 여기서 1이 carry이다. 
            carry = val // 10     #  7//10=0  #10//10=1      #8//10=0
            val = val % 10        #  7%10=7   #10%10=0       #8%10=8
            prev.next = ListNode(val) # we insert new ListNode, val는 방금 구한 수
                                  # 7         #0             #8
            # update pointers 
            prev = prev.next
            l1 = l1.next if l1 else None  # 다음 노드로 넘어가자
            l2 = l2.next if l2 else None  # 다음 노드로 넘어가자
            
        return dummy.next
'''
time complexity: O(max(n, m))
space complexity: O(max(n, m))
'''


# 입력
l1 = [2, 4, 3]
l2 = [5, 6, 4]

# 함수 호출을 위해 리스트를 ListNode로 변환
solution = Solution()
l1 = solution.array_to_linked_list(l1)
l2 = solution.array_to_linked_list(l2)

# 결과를 리스트로 변환하여 출력
result = solution.linked_list_to_array(solution.addTwoNumbers(l1, l2))
print(result)  # [7, 0, 8]

