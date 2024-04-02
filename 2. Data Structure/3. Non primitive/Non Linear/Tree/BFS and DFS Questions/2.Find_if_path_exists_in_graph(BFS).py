import collections
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        seen = [False] * n
        seen[source] = True
        q = collections.deque([source])
        while q:
            curr_node = q.popleft()
            if curr_node == destination:
                return True
            for next_node in graph[curr_node]:
                if not seen[next_node]:
                    seen[next_node] = True
                    q.append(next_node)
        return False          

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