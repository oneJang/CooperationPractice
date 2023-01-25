def reverse(x):
    res = 0
    while x > 0:
        t = x % 10
        res = res * 10 + t
        x = x // 10
    return res
    
def isPrime(x):
    if x == 1:
        return True
    for i in range(2, x//2+1):
        if x % i == 0:
            return False
    else:
        return True

n = int(input())
numList = list(map(int, input().split()))
prime = []

for x in numList:
    reversedNum = reverse(x)
    if isPrime(reversedNum):
        prime.append(reversedNum)
print(prime)