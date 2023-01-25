n = int(input())
count = 0
numList = [0]*(n+1)
for i in range(2, n+1):
    if numList[i] == 0:
        count += 1
        for j in range(i, n+1, i):
            numList[j] = 1
print(count)