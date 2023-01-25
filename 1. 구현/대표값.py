## 평균에 가장 가까운 애를 찾는데 평균에 가장 가까운 애가 몇 명 있으면 점수가 큰애, 점수가 큰애가 겹치면 번호가 빠른 애
## 문제 보면 번호랑 점수를 같이 따지므로 enumerate쓰면 편리한듯
## 평균과 가장 가까운애를 찾기 위해 min을 갱신해 나감
## 평균과 가장 가까운애가 여러명이면 점수를 비교하고 큰 애의 번호와 점수를 저장 
## 은근 생각하기 까다로운듯!!

n = int(input())
score = list(map(int, input().split()))
avg = sum(score)/len(score)
roundAvg = round(avg)
min = 21470000000

for idx, x in enumerate(score):
    temp = abs(roundAvg - x)
    if temp < min:
        min = temp
        sc = x
        num = idx + 1
    elif temp == min:
        if x > sc:
            sc = x
            num = idx + 1
print(sc, num)
