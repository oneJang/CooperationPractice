## 3개를 선택해서 나올 수 있는 모든 합의 경우를 따져보기 -> 3중 for문
## 중복되는거 제거를 위해 set을 사용했음
## 내림차순으로 정렬하고 k번째를 찾으면 될듯

n, k = map(int, input().split())
card = list(map(int, input().split()))
sumList = []

for i in range(n):
    for j in range(1+i, n):
        for k in range(2+j, n):
            sumList.append(card[i]+card[j]+card[k])

setList = set(sumList)
newList = list(setList)
newList.sort(reverse=True)
print(newList[k-1])
