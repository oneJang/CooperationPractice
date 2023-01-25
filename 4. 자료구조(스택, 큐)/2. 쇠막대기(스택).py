import sys
sys.stdin = open("input.txt", "r")
s = input()
list_s = list(s)
stack = []
summ = 0
for i in range(len(list_s)):
    if list_s[i] == "(":
        stack.append(i)
    else:
        if list_s[i-1] == "(":
            stack.pop()
            summ += len(stack)
        else:
            stack.pop()
            summ += 1
print(summ)