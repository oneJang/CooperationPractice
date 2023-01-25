# https://school.programmers.co.kr/learn/courses/30/lessons/43238
def solution(n, times):
    res = 0
    times.sort()
    start = times[0]
    end = max(times)*n
    
    while start <= end:
        mid = (start+end)//2 #임의의 시간
        possible = 0
        for x in times:
            possible += (mid // x) # 임의의 시간 안에 심사 가능한 사람 수
        if possible >= n: # 임의의 시간안에 심사 가능한 사람의 수가 심사 기다리는 사람 보다 같거나 많으면
            end = mid - 1 # 더 적은 시간에 심사가 가능하다는 뜻이므로 end = mid - 1
            res = mid
        else: #임의의 시간안에 심사 가능한 사람의 수가 심사 기다리는 사람 보다 적으면
            start = mid + 1 # 시간을 너무 짧게 잡았기 때문에 늘려야함 -> start = mid + 1
    return res