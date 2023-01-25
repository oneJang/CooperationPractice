# 그리디 알고리즘
# 탐욕적으로 해결하면 됨
# 현 상황에서 가장 좋은거를 선택하면 됨
# 어케?? 정렬 후 차례차례 좋은거 찾아가기
# 이 문제는 우선 회의가 끝나는 시간을 기준으로 정렬해야함
# 먼저 회의가 끝난 시간과 그 후 회의가 시작하는 시간을 맞춰야해
n = int(input())
times = []
for i in range(n):
    a, b = map(int, input().split())
    times.append((a, b))
times.sort(key = lambda x : (x[1], x[0]))
end = times[0][1]
meeting = []
meeting.append(times[0])
cnt = 1
for i in range(1, n):
    if times[i][0] == end:
        meeting.append(times[i])
        end = times[i][1]
        cnt += 1
print(cnt)
