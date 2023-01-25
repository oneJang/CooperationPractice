s = input()
stack = []

for i in s:
    if i.isdecimal():
        stack.append(int(i))
    else:
        count = 0
        if i == "+":
            a = stack.pop()
            b = stack.pop()
            stack.append(a+b)
        elif i == "-":
            a = stack.pop()
            b = stack.pop()
            stack.append(b-a)
        elif i == "*":
            a = stack.pop()
            b = stack.pop()
            stack.append(a*b)
        elif i == "/":
            a = stack.pop()
            b = stack.pop()
            stack.append(b/a)
        
print(stack[0])