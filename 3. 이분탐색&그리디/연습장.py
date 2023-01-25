from itertools import combinations
number = "1231234"
number_list = list(number)
k = 3
list_comb = []
case = len(number)-k
comb = list(combinations(number_list, case))
list_comb = list(map(list, comb))

for i in range(len(comb)):
    list_comb[i] = int("".join(list_comb[i]))
print(list_comb)
# print(max(list_comb))