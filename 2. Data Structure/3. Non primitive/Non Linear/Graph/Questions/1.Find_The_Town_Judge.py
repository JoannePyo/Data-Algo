'''
Input: n = 3            => 사람의 수
trust = [[1,3],[2,3]]   => [신뢰자. 신뢰받는자]
Output: 3 

                  0  1  2  3                        0  1  2  3 
trustor              1         => trustor              1  1     
vote_town_judge            1      vote_town_judge            2
                                                    n-1 => 3-1 => 2 그러므로 index3 출력. 
'''
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # 이는 모든 사람이 다른 사람을 믿어야 하므로 최소한 n - 1개의 신뢰 관계가 필요한 조건입니다.
        if len(trust) < n - 1:  # 만약 신뢰 관계의 수가 n - 1보다 작다면, 신뢰를 받는 사람을 찾을 수 없다고 판단.
            return -1  # -1 반환

        # 0으로 초기화.
        vote_town_judge = [0] * (n + 1)  # vote_town_judge. 신뢰를 몇명한테 받앗는지 세기  # 0
        trustor = [0] * (n + 1)  # trustor. 신뢰자가 몇명인지 세기      # 0

        # (a, b)가 주어지면, a는 b를 믿는 것이므로 trustor[a]를 증가시키고,
        # b는 a로부터 믿음을 받으므로 vote_town_judge[b]를 증가시킵니다.
        for a, b in trust:
            trustor[a] += 1          # trustor[1] = 1           => trustor[2] = 1
            vote_town_judge[b] += 1  # vote_town_judge[3]  = 3 => vote_town_judge[3]  = 2
        
        # 각 사람에 대해 vote_town_judge가 n - 1이고 trustor가 0이면, 그 사람은 모든 다른 사람으로부터 믿음을 받는 유일한 사람으로 판단됩니다.
        for i in range(1, n + 1):  # range(1,4)
            if vote_town_judge[i] == n - 1 and trustor[i] == 0:  # if (vote_town_judge)[3] == 3 and trustor[3]== 0
                return i  # 해당 사람의 인덱스를 반환                  # return 3
        
        # 만약 신뢰를 받는 사람이 없다면 -1을 반환
        return -1
'''
Time complexity: O(N+E)
Space complexity: O(N)
'''

# 입력
n = 3
trust = [[1,3],[2,3]]

# Solution 클래스의 인스턴스 생성
sol = Solution()

# 함수 호출하여 결과 출력
print(sol.findJudge(n, trust))