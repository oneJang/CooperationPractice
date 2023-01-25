# 리스트에서 s와 e 사이를 오름차순 정렬하고 k번째 숫자를 찾으면 될듯 ==> [:], sort..
t = int(input())
answer = []

while t:
    n, s, e, k = map(int, input().split())
    nlist = list(map(int, input().split()))
    new_List = nlist[s-1:e]
    new_List.sort()
    answer.append(new_List[k-1])
    t -= 1
for i in range(len(answer)):
    print("#%d %d"%(i+1, answer[i]))