# https://codeforces.com/problemset/problem/825/E

from collections import defaultdict, deque
from heapq import heappop, heappush


n, m = list(map(int, input().split()))


g = defaultdict(list)

outdeg = defaultdict(int)

for _ in range(m):
    u, v = list(map(int, input().split()))
    outdeg[u] += 1
    g[v].append(u)


heap = []
for i in range(1, n + 1):
    if outdeg[i] == 0:
        heappush(heap, -i)

res = defaultdict(int)

label = n

while heap:
    node = -heappop(heap)
    res[node] = label
    label -= 1

    for nei in g[node]:
        outdeg[nei] -= 1
        if outdeg[nei] == 0:
            heappush(heap, -nei)


for i in range(1, n + 1):
    print(res[i], end=" ")  
