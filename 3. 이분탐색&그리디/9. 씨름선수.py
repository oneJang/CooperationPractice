# 앞 문제에서 그리디는 대체로 "정렬"후 처리라고 했음
# 이 문제는 우선 키 큰순으로 정렬하고 몸무게를 비교하면됨
# 맨 앞의 몸무게를 최대로 지정하고 그거보다 큰 애가 있으면 걔를 포함시키면됨
n = int(input())
info = []
for i in range(n):
    a, b = map(int, input().split())
    info.append((a, b))
info.sort(reverse=True) # 키 순으로 정렬
max_weight = 0
cnt = 0
for w in info:
    if max_weight < w[1]:
        max_weight = w[1]
        cnt += 1
print(cnt)   