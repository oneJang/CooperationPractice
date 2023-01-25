## 문제에서 주어진대로 안푼거같은데..?
n, k = map(int, input().split())
count = 0

for i in range(1, n+1):
    if n % i == 0:
        count += 1
        if count == k:
            print(i)
            break