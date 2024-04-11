# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        import collections
        
        height_dict = collections.defaultdict(int)
        
        def insert(node, key):
            if not node:
                return TreeNode(key)
            if node.val < key:
                node.right = insert(node.right, key)
            elif node.val > key:
                node.left = insert(node.left, key)
            height_dict[node] = 1 + max(getHeight(node.left), getHeight(node.right))
            balance = getBalance(node)
            
            if balance > 1 and node.left.val > key:
                # LL imbalance -> Right Rotation
                return rightRotation(node)
            
            if balance > 1 and node.left.val < key:
                # LR imbalance -> Left Right Rotation
                node.left = leftRotation(node.left)
                return rightRotation(node)
            
            if balance < -1 and node.right.val < key:
                # RR imbalance -> Left Rotation
                return leftRotation(node)
            
            if balance < -1 and node.right.val > key:
                # RL imbalance -> Right Left Rotation
                node.right = rightRotation(node.right)
                return leftRotation(node)
            
            return node
            
        def getHeight(node):
            if not node:
                return 0
            return height_dict[node]
        
        def getBalance(node):
            if not node:
                return 0
            return getHeight(node.left) - getHeight(node.right)
        
        def rightRotation(node):
            new_node = node.left
            subtree = new_node.right
            new_node.right = node
            node.left = subtree
            new_node.height = 1 + max(getHeight(new_node.left), getHeight(new_node.right))
            node.height = 1 + max(getHeight(node.left), getHeight(node.right))
            return new_node
        
        def leftRotation(node):
            new_node = node.right
            subtree = new_node.left
            new_node.left = node
            node.right = subtree
            new_node.height = 1 + max(getHeight(new_node.left), getHeight(new_node.right))
            node.height = 1 + max(getHeight(node.left), getHeight(node.right))
            return new_node
        
        return insert(root, val)


# 주어진 리스트를 이진 탐색 트리로 변환하는 함수
def listToBST(arr):
    if not arr:
        return None
    root = TreeNode(arr[0])
    for val in arr[1:]:
        solution.insertIntoBST(root, val)
    return root

root = listToBST([4, 2, 7, 1, 3])

val = 5
solution = Solution()
print(solution.insertIntoBST(root,val))  # 출력: [4,2,7,1,3,5]
