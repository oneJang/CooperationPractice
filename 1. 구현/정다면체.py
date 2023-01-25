n, m = map(int, input().split())

countList = [0]*(n+m+3)
max = -99999999

for i in range(1, n+1):
    for j in range(1, m+1):
        countList[i+j] += 1

for i in range(n+m+1):
    if countList[i] > max:
        max = countList[i]
for i in range(n+m+1):
    if countList[i] == max:
        print(i, end=' ')
