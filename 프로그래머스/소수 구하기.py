from itertools import combinations

def isprime(x):
    for i in range(2, x):
        if x%i==0:
            return False
    return True

def solution(nums):
    answer = 0
    comb = list(combinations(nums, 3))
    sum_num = list(map(sum, comb))

    for x in sum_num:
        if isprime(x):
            answer += 1
    return answer

print(solution([1, 2, 7, 6, 4]))