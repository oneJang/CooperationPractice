n = int(input())
array = list(map(int, input().split()))
left = 0
right = n-1
last = 0
res = ""
tmp=[]
while left<=right:
    if array[left] > last:
        tmp.append((array[left], 'L'))
    if array[right] > last:
        tmp.append((array[right], 'R'))
    array.sort()
    if len(tmp)==0:
        break
    else:
        res += tmp[0][1]
        last = tmp[0][0]
        if tmp[0][1]=='L':
            left += 1
        else:
            right -= 1
    tmp.clear()
print(len(res))
print(res)