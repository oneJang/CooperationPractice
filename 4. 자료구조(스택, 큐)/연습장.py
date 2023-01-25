n = 1001
n = str(n)
n_list = list(map(int, n))
print(n_list)
n_list.remove(0)
print(n_list)
n_list = [str(i) for i in n_list]
print(int("".join(n_list)))

a = "101"
print(a)