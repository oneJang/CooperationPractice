def digit_sum(x):
    str_x = str(x)
    total = 0
    for i in str_x:
        total += int(i)
    return total


n = int(input())
numList = list(map(int, input().split()))
sumList = []
max = -99999
for idx, num in enumerate(numList):
    X = digit_sum(num)
    if X > max:
        max = X
        index = idx
print(numList[idx])