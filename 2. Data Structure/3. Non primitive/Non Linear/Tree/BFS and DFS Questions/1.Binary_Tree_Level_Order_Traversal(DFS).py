class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        
        def helper(node, level):
            # start the current level
            if len(res) == level:
                res.append([])

            # append the current node value
            res[level].append(node.val)

            # process child nodes for the next level
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)
            
        helper(root, 0)
        return res
'''
Time complexity: O(N) since each node is processed exactly once.
Space complexity: O(N) to keep the output structure which contains N node values.
'''
from collections import deque
def build_tree(nodes):
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = deque([root])
    i = 1
    while queue:
        node = queue.popleft()
        if i < len(nodes) and nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            queue.append(node.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            node.right = TreeNode(nodes[i])
            queue.append(node.right)
        i += 1
    return root

root = [3, 9, 20, None, None, 15, 7]
tree_root = build_tree(root)

solution = Solution()
print(solution.levelOrder(tree_root))  # 출력: [[3], [9, 20], [15, 7]]