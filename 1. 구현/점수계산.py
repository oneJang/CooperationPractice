n = int(input())
ox = list(map(int, input().split()))
length = len(ox)
count = 0
score = []

for o in ox:
    if o:
        count += 1
    else:
        count = 0
    score.append(count)
print(sum(score))