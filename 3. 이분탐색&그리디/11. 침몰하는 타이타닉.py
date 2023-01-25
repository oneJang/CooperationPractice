# 해설풀이로는 오름차순으로 정렬해서 젤 큰애랑 젤 작은애랑 더해서 제한을 넘는가 아닌가를 판단하고 pop시키는건데.. 이게 맞는건가
# 일단 내 풀이: 내림차순으로 정렬하고 젤 큰애 + 나머지 하나하나 비교ㅋㅋ

# n, m = map(int, input().split())
# weights = list(map(int, input().split()))
# full = [0]*n
# boat = 0
# weights.sort(reverse=True)

# for i in range(n):
#     if full[i] == 0:
#         full[i] = 1
#     else:
#         continue
#     total = weights[i]
#     for j in range(1, n):
#         if total + weights[j] <= m and full[j] == 0:
#             total += weights[j]
#             full[j] = 1
#     if total <= m:
#         boat += 1
# print(boat)
from collections import deque
n, m = map(int, input().split())
weights = list(map(int, input().split()))
weights.sort()
weights = deque(weights)
boat = 0
while weights:
    if len(weights) == 1:
        boat += 1
    if weights[0] + weights[-1] > m:
        weights.pop()
        boat += 1
    else:
        weights.pop()
        weights.popleft()
        boat += 1
print(boat)
