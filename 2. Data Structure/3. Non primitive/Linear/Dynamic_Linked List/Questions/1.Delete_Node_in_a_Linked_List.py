'''
There is a singly-linked list head and we want to delete a node node in it.

You are given the node to be deleted node. You will not be given access to the first node of head.

All the values of the linked list are unique, and it is guaranteed that the given node node is not the last node in the linked list.

Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:

The value of the given node should not exist in the linked list.
The number of nodes in the linked list should decrease by one.
All the values before node should be in the same order.
All the values after node should be in the same order.
Custom testing:

For the input, you should provide the entire linked list head and the node to be given node. node should not be the last node of the list and should be an actual node in the list.
We will build the linked list and pass the node to your function.
The output will be the entire list after calling your function.
'''
'''
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, 
the linked list should become 4 -> 1 -> 9 after calling your function.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteNode(node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    
    node_next = node.next  # 주어진 노드의 다음 노드를 가리키는 포인터를 저장합니다.
    node.val = node_next.val  # 다음 노드의 값을 현재 노드로 복사합니다.
    node.next = node_next.next  # 현재 노드의 다음 노드를 다음 다음 노드로 설정하여 다음 노드를 건너뛰빈다.
    #del(node_next)  # 삭제할 다음 노드를 메모리에서 제거합니다.

# 주어진 입력 리스트를 연결 리스트로 변환합니다.
def list_to_linkedlist(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for item in lst[1:]:
        current.next = ListNode(item)
        current = current.next
    return head

# 연결 리스트를 리스트로 변환합니다.
def linkedlist_to_list(head):
    lst = []
    current = head
    while current:
        lst.append(current.val)
        current = current.next
    return lst

# 주어진 입력 데이터를 사용하여 연결 리스트를 생성합니다.
head_data = [4, 5, 1, 9]
node_val = 5
# 연결 리스트로 변환합니다.
head = list_to_linkedlist(head_data)
# 삭제할 노드를 찾습니다.
current = head
while current:
    if current.val == node_val:
        break
    current = current.next
# 노드 삭제를 호출합니다.
if current:
    deleteNode(current)
# 결과를 출력합니다.
result = linkedlist_to_list(head)
print(result)


'''
time complexity: O(1)
space complexity: O(1)
'''