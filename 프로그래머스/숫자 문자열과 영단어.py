answer = 0
s = "one4seveneight"
temp = ''
num_alpha = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
left = 0
right = 1
while right <= len(s):
    if s[left:right] in num_alpha:
        temp += num_alpha[s[left:right]]
        left = right
        print(temp)
    else:
        if s[left:right] in num:
            temp += s[left:right]
            print(temp)
    right += 1