# Daily_Temperatures (Medium)

Given an array of integers `temperatures` represents the daily temperatures, return *an array* `answer` *such that* `answer[i]` *is the number of days you have to wait after the* `ith`  *day to get a warmer temperature* . If there is no future day for which this is possible, keep `answer[i] == 0` instead.

**Example 1:**

```
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```

**Example 2:**

```
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
```

**Example 3:**

```
Input: temperatures = [30,60,90]
Output: [1,1,0]
```

## **Monotonic Stack이란**

모노토닉 스택(Monotonic Stack)은 스택 자료 구조를 기반으로 한 특별한 형태의 스택입니다. 이 스택은 원소를 넣을 때나 뺄 때 특정한 규칙에 따라 모노토닉한 증가 또는 감소를 유지하는 스택입니다. 주로 알고리즘 문제 해결에 사용되며, 주로 다음과 같은 두 가지 유형이 있습니다:

1. 모노토닉 증가 스택: 스택에 원소를 넣을 때, 현재 원소보다 큰 원소가 스택 내부에 존재하지 않도록 유지합니다. 이렇게 하면 스택 내부에서 가장 작은 원소가 항상 맨 위에 위치하게 됩니다.
2. 모노토닉 감소 스택: 스택에 원소를 넣을 때, 현재 원소보다 작은 원소가 스택 내부에 존재하지 않도록 유지합니다. 이렇게 하면 스택 내부에서 가장 큰 원소가 항상 맨 위에 위치하게 됩니다.

모노토닉 스택은 주로 스택을 이용하여 배열이나 리스트 등의 데이터 구조에서 특정 조건을 만족하는 원소를 효율적으로 찾을 때 사용됩니다. 주로 최대, 최소값 찾기나 슬라이딩 윈도우 문제 등에 적용됩니다.
