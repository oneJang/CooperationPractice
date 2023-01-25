s = input()
alpha = []
num = []

for i in s:
    if i.isalpha():
        alpha.append(i)
    else:
        num.append(int(i))
alpha.sort()


answer = ''.join(alpha + list(str(sum(num))))
print(answer)