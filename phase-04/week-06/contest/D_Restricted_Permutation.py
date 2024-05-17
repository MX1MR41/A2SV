"""

https://codeforces.com/gym/520390/problem/D

"""

import heapq

N, M = map(int, input().split())
indeg = [0] * N
out = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    indeg[b] += 1
    out[a].append(b)

heap = []
for i in range(N):
    if indeg[i] == 0:
        heapq.heappush(heap, i)

ans = []
while heap:
    i = heapq.heappop(heap)
    ans.append(i)
    for j in out[i]:
        indeg[j] -= 1
        if indeg[j] == 0:
        	heapq.heappush(heap, j)

if len(ans) != N:
    print(-1)
else:
    print(*[x + 1 for x in ans])