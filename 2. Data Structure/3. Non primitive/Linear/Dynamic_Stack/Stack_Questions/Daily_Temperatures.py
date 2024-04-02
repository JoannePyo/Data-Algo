from typing import Optional, List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures) # 입력된 온도 리스트의 길이를 구합니다.
        answer = [0] * n      # 결과를 저장할 리스트를 만들고, 초기값을 0으로 설정합니다.
        stack = []

        for curr_day, curr_temp in enumerate(temperatures): #입력된 온도 리스트를 순회하면서 각 날짜와 온도를 가져옵니다.
            #스택이 비어있지 않고, 스택의 맨 위에 있는 날짜의 온도가 현재 온도보다 낮을 때까지 반복합니다.
            while stack and temperatures[stack[-1]] < curr_temp:
                prev_day = stack.pop()
                answer[prev_day] = curr_day - prev_day #현재 날짜에서 이전에 스택에 저장된 날짜를 뺀 값이, 이전 날짜부터 현재 날짜까지의 날짜 차이입니다. 이 값을 결과 리스트에 저장합니다.
            stack.append(curr_day) #현재 날짜를 스택에 추가합니다.

        return answer #계산된 결과를 반환합니다.

solution = Solution()
temperatures = [73,74,75,71,69,72,76,73]
print(solution.dailyTemperatures(temperatures))

'''
Time Complexity: 
Space Complexity: 
'''