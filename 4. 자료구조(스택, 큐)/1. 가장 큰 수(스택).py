#stack의 마지막 인덱스랑 현재 숫자랑 비교해서 현재 숫자가 크면 stack의 마지막꺼는 pop시키고 지우는 횟수를 감소시키는데 마지막꺼가 현재숫자보다 작은 동안에는 pop을 반복한다.
# 그리고 현재 숫자를 stack에 추가한다.
# 근데 지우는 횟수를 다 감소시키기 전에 stack에 숫자를 다 담았다면 못지운 수만큼 stack의 뒤에서 부터 떨군다.
import sys
sys.stdin=open('input.txt', 'r')
n, m = map(int, input().split())
n_list = list(map(int, str(n)))
stack = []
for i in n_list:
    while stack and m>0 and stack[-1]<i:
        stack.pop()  
        m -= 1      
    stack.append(i)
if m != 0:
    stack = stack[:-m]
result = "".join(map(str, stack))
print(result)