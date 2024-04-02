class Node:
    def __init__(self, data=None):
        # 초기값 만들기. 데이타는 데이타이고 next pointer은 next.
        self.data = data
        self.next = next

# make nodes
node1= Node(1)
node2 = Node(2)
node3 = Node(3)

# add node
node1.next = node3
node3.next = node2

# head 정하기
head = node1

print(node1.data)  # 1
print(node1.next)  # <__main__.Node object at 0x7fa39003abb0>
print(node1.next.data) # 3
print(node2.data)      # 2
print(node2.next)      # <built-in function next>
print(node3.next.data) # 2