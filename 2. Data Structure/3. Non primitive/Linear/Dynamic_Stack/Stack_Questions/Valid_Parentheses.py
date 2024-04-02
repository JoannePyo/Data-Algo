'''
'(' , ')' , '{' , '}' , '[' , ']'  
Input: s = "()[]{}"
Output: true
'''

class Solution(object):
    def isValid(self, s):
        stack = [] #스택과 괄호들의 대응 관계를 저장하는 해시 맵을 생성합니다.
        mapping = {")": "(", "}": "{", "]": "["} #여는 괄호를 키로 하고 닫는 괄호를 값으로 하여 대응 관계를 나타냅니다.

        for char in s: #주어진 문자열 s를 한 글자씩 반복합니다.
            if char in mapping: #현재 글자가 닫는 괄호인지 확인합니다.
                top_ele = stack.pop() if stack else "#" #스택이 비어있지 않다면 스택에서 가장 위에 있는 요소를 꺼내고, 비어있다면 '#'를 반환합니다.
                if mapping[char] != top_ele: #현재 닫는 괄호의 대응되는 여는 괄호와 스택의 맨 위 요소가 일치하지 않는지 확인합니다.
                    return False  #일치하지 않으면 유효하지 않은 괄호 문자열이므로 False를 반환합니다.
            else:                 
                stack.append(char)  #현재 글자가 여는 괄호인 경우에는 스택에 추가합니다.
        return not stack
    #반복이 끝난 후 스택이 비어있는지 확인하여, 비어있다면 올바른 괄호 문자열이므로 True를 반환하고, 비어있지 않다면 괄호가 제대로 닫히지 않은 것이므로 False를 반환합니다.

# 주어진 문자열
s = "(){}[]"

# Solution 객체 생성
solution = Solution()

# isValid 함수 호출하여 결과 출력
print(solution.isValid(s))




'''
Time Complexity: O(n)
Space Complexity: O(n)
'''
