n, m = map(int, input().split())
height = list(map(int, input().split()))
height.sort()
start = 0
end = max(height)
result = 0

while start <= end:
    mid = (start+end)//2
    consumer = 0
    for i in height:
        if i - mid > 0:
            consumer += (i - mid)
    if consumer >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)