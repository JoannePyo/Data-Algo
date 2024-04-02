# 테스트
head = [[1, 1], [2, 1]]

solution = Solution()
copied_head = solution.copyRandomList(head)

# 결과 출력
result = []
cur = copied_head
while cur:
    random_val = cur.random.val if cur.random else None
    result.append([cur.val, random_val])
    cur = cur.next

print(result)
