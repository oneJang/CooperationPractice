def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2+1):
        prev = s[:i]
        data = ""
        count = 1
        for j in range(i, len(s), i):
            if prev == s[j:j+1]:
                count += 1
            else:
                data += str(count) + prev if count >= 2 else prev
                prev = s[j:j+1]
                count = 1
        data += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(data))
    return answer
print(solution("aabbacc"))