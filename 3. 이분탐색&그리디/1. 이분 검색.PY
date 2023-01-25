# binary search
# list의 맨 첫과 맨 끝을 정하고(left, right) 2로 나눈 몫을 mid로 설정!
# 찾고자 하는 값이 mid보다 작은지 큰지 비교하면 어느 영역에 있는지 알 수 있음(mid보다 작은 영역 or mid보다 큰 영역)
# 만약에 찾고자 하는 값이 mid보다 작다면 right가 mid-1로 옴
# 만약에 찾고자 하는 값이 mid보다 크다면 left가 mid+1로 옴
# --> 이런식으로 절반씩 툭툭 범위를 줄여가며 찾는 알고리즘을 binary search라고 함(O(logn))

n, m = map(int, input().split())
list = list(map(int, input().split()))
list.sort()
left = 0
right = n-1

while left <= right:
    mid = (left + right) // 2
    if list[mid] == m:
        print(mid+1)
        break
    elif list[mid] > m:
        right = mid - 1
    else:
        left = mid + 1