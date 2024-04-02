class Node:
    def __init__(self, data, next=None): 
        self.data = data  
        self.next = next

# add 함수 정의
def add(data):
    global head  # head 변수를 전역 변수로 사용
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)

# Node1 생성해보기
node1 = Node(1)
node2 = Node(2)

# 가장 맨 앞 Node를 알기 위해 head 지정
head = node1

node1.next = node2

# add 함수 통해 신규 노드 추가하기
add(3)

# 추가한 값을 node1 통해 next로 출력해보기
print(node1.next.data)  # 2
print(node2.next.data)  # 3