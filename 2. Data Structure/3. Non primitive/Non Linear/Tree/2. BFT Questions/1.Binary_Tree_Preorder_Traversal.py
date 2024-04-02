'''
Input: root = [1,null,2,3]
Output: [1,2,3]

(Data→ Left → Right) L

    1
  /   \
2       3
      /   \
    4       5
'''

# iteration
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List

class Solution:
    def preorderTraversal(self, root) -> List[int]:
        stack =[]
        res=[]
        curr = root

        while stack or curr:             # curr = 1    # stack=[3]        # stack =[3.null]   # stack =[3]  # curr= 3       # curr=4           # stack =[5,null]  #stack =[5]  # curr=5           # 둘다 null
            if curr:                                                      # null              # null        # 3             # 4                # null                          # 5
                res.append(curr.val)     # res = [1]   # res = [1.2]                                        # res= [1,2,3]  # res = [1,2,3,4]                                  # rest=[1,2,3,4,5]
                stack.append(curr.right) # stack= [3]  # stack =[3.null]                                    # stack =[5]    # stack =[5,null]                                  # stack = [null]
                curr = curr.left         # curr = 2    # curr = null                                        # curr= 4       # null                                             # null
            else:
                curr = stack.pop()                                       # curr = null빼기     # curr= 3빼기                                      # curr= null빼기   # curr= 5빼기                     
        return res                                                                                                                                                                                  # res=[1,2,3,4,5]
