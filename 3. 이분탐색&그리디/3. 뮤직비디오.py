def count(capacity):
    cnt = 1
    sum = 0
    for x in songs:
        if sum + x > capacity:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt

n, m = map(int,input().split())
songs = list(map(int,input().split()))

start = 1
end = sum(songs)
maxx = max(songs)

while start <= end:
    mid = (start+end)//2
    if mid >= maxx and count(mid) <= m:
        res=mid
        end = mid - 1
    else:
        start = mid + 1
print(res)