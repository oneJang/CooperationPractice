# from collections import deque
# n, k = map(int, input().split())
# princes = [i for i in range(1, n+1)]
# queue = deque(princes)
# count = 1
# while queue and count <= 3 and len(queue) != 1:
#     if count == k:
#         queue.popleft()
#         count = 1
#     else:
#         a = queue.popleft()
#         queue.append(a)
#         print(queue, count)
#         count += 1
# print(queue)
from collections import deque
n, k = map(int, input().split())
princes = list(range(1, n+1))
queue = deque(princes)
while queue:
    for _ in range(k-1):
        a = queue.popleft()
        queue.append(a)
    queue.popleft()
    if len(queue)==1:
        print(queue[0])
        queue.popleft()