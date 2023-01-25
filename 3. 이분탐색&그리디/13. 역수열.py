# 역수열에서 원래 수열을 찾아내는 문제
# 0으로 초기화된 n 길이의 리스트를 만들고 거기에 원래 수열을 만들거임
# 1부터 차례차례 자기보다 큰 애가 몇개인지를 빈칸의 개수로 생각하면될듯
n = int(input())
re_array = list(map(int, input().split()))
array = [0]*n
for i in range(n):
    for j in range(n):
        if re_array[i]==0 and array[j]==0:
            array[j]=i+1
            break
        elif array[j]==0:
            re_array[i] -= 1