'''
203. Remove Linked List Elements

Given the head of a linked list and an integer val, remove all the nodes of the linked list 
that has Node.val == val, and return the new head.
'''
'''
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

더미 == ListNode(0) -> head == ListNode(1) == 1 ->  ListNode(2) ==2
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """


        node = ListNode(0) # ListNode(0)가 새로운 연결 리스트의 첫 번째 노드가 되고, 이 노드는 더미 노드(dummy node)입니다. 
        node.next = head # head는 ListNode(1)을 가리키며, 실제 데이터가 있는 첫 번째 노드입니다.
        
        prev, curr = node, head  #prev = dummy, curr = 1         
        while curr:                   # 1                # 2         # 6                # 3 
            if curr.val == val:       # 1 != 6           # 2 != 6    # 6 == 6           # 3 != val
                prev.next = curr.next                                # prev.next = 3
            else:  
                prev = curr           # dummy -> 1       # 1 => 2                       # prev = 3
            curr = curr.next          # current 는 2가 됨. # 2 => 6    # 6 => 3           # 3 = 4 ...
        
        return node.next # node.next를 반환하면, 더미 노드를 제외한 첫 번째 노드 ListNode(1)부터 시작하는 연결 리스트가 반환됩니다.

# 연결 리스트 생성
head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
val = 6

# Solution 객체 생성
solution = Solution()
result = solution.removeElements(head, val)

# 결과 출력
while result:
    print(result.val)
    result = result.next

'''
time complexity: O(n) 한번만 순회하면서 각 노드를 확인하고 제거.
space complexity: O(1) 추가적인 공간을 사용하지 않고 주어진 연결 리스트를 수정.
'''