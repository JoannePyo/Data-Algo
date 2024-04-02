import collections
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)  # defaultdict(<class 'list'>, {})
        for a, b in edges:
            graph[a].append(b)                 #{0: [1]}         #{0: [1], 1: [0, 2]          #{0: [1], 1: [0, 2], 2: [1, 0]}
            graph[b].append(a)                 #{0: [1], 1: [0]} #{0: [1], 1: [0, 2], 2: [1]} #{0: [1, 2], 1: [0, 2], 2: [1, 0]
            
        seen = [False] * n                          #[False, False, False]
        
        def dfs(curr_node):                         #0                                  #1                                  #0                                              #2
            if curr_node == destination:            #False                              #False                              #False                                          #True
                return True                                                                                                                                                 #return True
            if not seen[curr_node]:                #not seen[0]                         #not seen[1]                        #not seen[0]=>False
                seen[curr_node] = True             #seen[0] = True [True, False, False] #seen[1] = True [True, True, False]
                for next_node in graph[curr_node]: #next_node = 1 in graph[0]           #next_node =0 in graph[1]                                 #next_node=2 in graph[1]  
                    if dfs(next_node):             # dfs(1)                             #dfs(0)                                                                             #dfs(2)
                        return True                                                                                                                                         #return True....
            return False                                                                                                    #False                                               
            
        return dfs(source)
    
'''
Time complexity: O(n+m) 
Space complexity: O(n+m)
'''

n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2

solution = Solution()
print(solution.validPath(n, edges, source, destination))