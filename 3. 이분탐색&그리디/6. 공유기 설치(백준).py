# https://acmicpc.net/problem/2110
n, c = map(int, input().split())
house = []
for i in range(n):
    house.append(int(input()))
house.sort()
start = house[0]
end = max(house)
result = 0

def count(mid):
    s = house[0]
    res = 1
    for i in range(1, len(house)):
        if house[i] - s < mid:
            continue
        else:
            res += 1
            s = house[i]
    return res

while start <= end:
    mid = (start+end)//2
    if count(mid) >= c:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)