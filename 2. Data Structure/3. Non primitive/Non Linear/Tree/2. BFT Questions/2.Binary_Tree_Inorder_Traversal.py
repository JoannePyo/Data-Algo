
'''
  1
2   3 

'''
#     Left → Data → Right   o(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

class Solution:
    def inorderTraversal(self, root) -> List[int]:
        res = []
        stack = []
        curr = root

        while curr or stack:  # 둘다 안비면                                # stack 안 빔 .                   # 다시 온 while에서 stack에 값이 있음   # curr = 3     # stack =[3]
            while curr: # current 안비면                                  # current null임.                # current null임                   # curr =3      # curr = null
                stack.append(curr) # stack에 현재 값 저장. stack=[1] =>[1,2]                                                                    # stack =[3]
                curr = curr.left   # left로 가.                2   => null                                                                     # null
            curr = stack.pop()                                           # stack =[1,2]에서 2뺌            # 1                                              # stack = [3]
            res.append(curr.val)                                         # res = [2]                     # res = [2,1]                                    # res = [2,1,3]
            curr = curr.right                                            # curr노드에 right node 값을 봐 curr=null. 다시 맨처음 while  # 1에 right는 3.          #  null
        return res


