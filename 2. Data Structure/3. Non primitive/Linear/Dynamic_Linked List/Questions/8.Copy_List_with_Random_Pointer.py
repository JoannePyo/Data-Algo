# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):

# 1st pass
        # adding it to the hashmap. Not connecting the pointers yet!
        clone = {None: None}  # every single old node to the copy of that node that we create.
        curr = head

        while curr:  # until this current pointer reaches the end of the linked list. when the current node becomes null.
            copy = Node(curr.val)  # creating a clone of the node a deep copy of the node putting it in copy.
            # this copy put it in hash map
            clone[curr] = copy  # map the old node to the copy
            curr = curr.next  # current pointer until it reaches null and the first pass of our loop is going to be done.

        # 2nd pass
        curr = head
        while curr:
            # now I'm going to set the pointers
            copy = clone[curr]  # this copy gives us current old copy node.
            copy.next = clone[curr.next]  # map original nodes to the copies, so if we take cur.next,
            # that's gonna map us to the copy of of current.next. that i created, and that copy can be stored
            # in copy.next.If is null, clone = {None: None}을 써준다. 그러므로 마지막에 node를 null로 써줄수 있다.
            copy.random = clone[curr.random]
            curr = curr.next

        return clone[head]  # return the head of the copy list.
        # how? we can take the head of the original linked list and then map it to the copy
        # and then return that head of the copylist.
    
'''
Time Complexity: O(n)
왜냐하면 두 번의 패스를 사용하여 주어진 연결 리스트의 모든 노드를 한 번씩만 방문하기 때문입니다. 
첫 번째 패스에서는 각 노드를 복제하고 해시맵에 저장하며, 두 번째 패스에서는 각 노드의 포인터를 설정합니다. 이 과정에서 각 노드는 한 번만 처리되므로 시간 복잡도는 선형입니다.

Space Complexity: O(n)
왜냐하면 복제된 각 노드에 대한 해시맵을 사용하여 추가적인 메모리를 사용하기 때문입니다. 
따라서 연결 리스트의 노드 수에 비례하여 공간이 증가합니다.
'''    