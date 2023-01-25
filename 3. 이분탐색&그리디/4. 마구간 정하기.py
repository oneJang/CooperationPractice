n, c = map(int, input().split())
location = []
for i in range(n):
    location.append(int(input()))
location.sort()
start = 1
end = max(location)
def count(mid):
    batch = location[0]
    res = 1
    for i in range(1, len(location)):
        if location[i] - batch < mid:
            continue
        else:
            batch = location[i]
            res += 1
    return res
while start <= end:
    mid = (start+end)//2
    if count(mid) >= c:
        res = mid
        start = mid + 1
    if count(mid) < c:
        end = mid - 1
print(res)