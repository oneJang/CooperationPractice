# binary search의 활용 문제!
k, n = map(int, input().split())
line = []
for i in range(k):
    line.append(int(input()))
start = 0
end = max(line)-1

while start <= end:
    mid = (start+end)//2
    count = 0
    for i in line:
        count += (i // mid)
    if count < n:
        end = mid - 1
    elif count >= n:
        res = mid
        start = mid + 1
print(res)
