'''
Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.
'''
'''
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        visited = set()          #initialize hashset.
        while head is not None:     # head가 none이 아니면. condition check if the head node is already inside of hash set.
            if head in visited:  # hashset에 있으면 it already been visited
                return True         # return True. Cycle.

            visited.add(head)    # hashset에 없으면 add 하기. 
            head = head.next        # head가 다음 노드로. 
        return False
				# head node 가 equal to null 될때까지 체크. 만약 null이면 that we've reached the ending of our linked list.
				# that means we do not have a cycle. 

# Time Complexity  -> O(n)
# Space complexity -> O(n)
    
# 주어진 입력에 대한 테스트
def create_linked_list_with_cycle(arr, pos):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    cycle_node = None
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
        if i == pos:
            cycle_node = current
    if cycle_node:
        current.next = cycle_node
    return head

head = create_linked_list_with_cycle([3, 2, 0, -4], 1)

solution = Solution()
print(solution.hasCycle(head))