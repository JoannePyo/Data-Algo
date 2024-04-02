'''
    3           [ [3]
  /   \
9      20          [9,20]
       / \
    15     7       [15, 7]  ]
'''
import collections
from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root) -> List[List[int]]:
        res = []  # 결과를 저장할 리스트

        q = collections.deque()  # 덱(deque) 자료구조를 사용하여 큐를 생성          # Queue[]
        q.append(root)  # 초기에 루트 노드를 큐에 추가                             # Queue =[3]

        while q:  # 큐가 비어있지 않은 동안 반복                                   # Queue =[3] #[9,20]               #[15,7]
            len_q = len(q)  # 현재 큐의 길이를 저장 (현재 레벨에 있는 노드 수).        # 1          # 2                   # 2
            level = []  # 현재 레벨의 노드 값을 저장할 리스트. one level at a time   # empty      # []                  # []

            for i in range(len_q):  # 현재 레벨에 있는 노드 수만큼 반복             # 1번 반복     #2                    # 2
                node = q.popleft()  # 큐에서 노드를 하나 꺼냄. FIFO               # 3를 꺼냄     #9    #20             # 15   #7

                if node:  # 노드가 존재하는 경우                                  
                    level.append(node.val)  # 노드의 값을 현재 레벨 리스트에 추가    # level =[3] #[9]  #[9,20]         #[15]  #[15,7]
                    q.append(node.left)  # 노드의 왼쪽 자식을 큐에 추가            # q =[9]     # null #[15]          #null   #null
                    q.append(node.right)  # 노드의 오른쪽 자식을 큐에 추가          # q=[9,20]   # null #[7]           #null  #null
            if level: # if level is not empty
                res.append(level)  # 현재 레벨의 노드 값을 결과 리스트에 추가         #res=[3]             #[[3],[9,20]]         #[3],[9,20], [15,7]]   

        return res  # 최종 결과 반환                                                                                       #[3],[9,20], [15,7]]
    

'''
Time complexity: O(N) since each node is processed exactly once.
Space complexity: O(w) to keep the output structure which contains N node values.
'''