'''
Remove Nth Node From End of List(Medium)

Given the head of a linked list, remove the nth node from the end of the list and return its head.
'''
'''
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Input: head = [1,2], n = 1
Output: [1]
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):  # n= 2
        dummy = ListNode(0, head)
        prev, curr = dummy, head

        while 0 < n and curr:  # 2>0       1>0
            curr = curr.next  # 1->2      2 ->  3
            n -= 1  # 2-=1==1   1-=1==0

        while curr:  # null
            prev = prev.next  # dummy=1  #1=2
            curr = curr.next  # 3=4     #4=5

        # delete
        prev.next = prev.next.next  # left =3; 3 = 5  (4 지워짐)

        return dummy.next  # 1->2->3->5
    
    '''
    time complexity: O(n) 
    space complexity: O(1) 
    '''

# 주어진 입력
head_values = [1, 2, 3, 4, 5]
n = 2

# 연결 리스트 생성
head = ListNode(head_values[0])
current = head
for value in head_values[1:]:
    current.next = ListNode(value)
    current = current.next

# 주어진 함수 호출
solution = Solution()
result_head = solution.removeNthFromEnd(head, n)

# 결과 출력
result_values = []
current = result_head
while current:
    result_values.append(current.val)
    current = current.next

print(result_values)  # 출력: [1, 2, 3, 5]


