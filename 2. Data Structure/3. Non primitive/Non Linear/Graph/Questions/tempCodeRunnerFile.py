from collections import defaultdict
from typing import Optional, List

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        maxRank = 0  # 최대 네트워크 랭크를 저장할 변수를 초기화합니다. #도로의 총수
        adj = defaultdict(set)  # 각 도시의 연결된 도시들을 저장할 defaultdict를 생성합니다.
        # 기본값이 빈 집합(set)인 딕셔너리를 생성하는 것. 각 도시를 키(key)로 사용하고, 
        # 그 도시와 직접적으로 연결된 다른 도시들의 집합을 값(value)으로 가지는 딕셔너리를 만들게 됩니다.

        # 주어진 도로 정보를 토대로 adj 리스트를 만듭니다.
        for road in roads:
            adj[road[0]].add(road[1]) # 두개의 도시를 연결하므로 [0,0]이 아닌 [0,1]부터이다.
                                      # adj[road[0]]은 첫 번째 도시와 연결된 다른 도시들의 집합이 되고,
                                      # 여기에 add(road[1])이라고 하면 두 번째 도시를 추가한다는 뜻이에요.
            adj[road[1]].add(road[0]) # 반대로 양쪽이 연결되는것. 위에가 [0,1] 이면 여기는 [1,0]이라는 뜻.

        # 모든 가능한 도시 쌍에 대해 반복합니다.
        for node1 in range(n):
            for node2 in range(node1 + 1, n):   # node1보다 큰 값부터 n-1까지
                # 현재 도시 쌍의 네트워크 랭크를 계산합니다.
                currentRank = len(adj[node1]) + len(adj[node2])  # len(adj[node1])은 첫 번째 도시와 연결된 다른 도시의 수를 나타내고,
                                                                 # len(adj[node2])는 두 번째 도시와 연결된 다른 도시의 수

                # 만약 두 도시가 이미 연결되어 있다면, 중복으로 세어지는 것을 방지하기 위해 1을 빼줍니다.
                if node2 in adj[node1]:
                    currentRank -= 1

                # 현재 도시 쌍의 네트워크 랭크가 최대 랭크보다 크다면 최대 랭크를 업데이트합니다.
                maxRank = max(maxRank, currentRank)

        # 최대 네트워크 랭크를 반환합니다.
        return maxRank

# 입력
n = 5
roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]

# Solution 클래스의 인스턴스 생성
sol = Solution()

# 함수 호출하여 결과 출력
print(sol.maximalNetworkRank(n, roads))