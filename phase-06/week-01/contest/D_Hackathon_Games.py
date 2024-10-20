from collections import defaultdict
from heapq import heapify, heappop, heappush


N, M = map(int, input().split())
G = defaultdict(list)

for _ in range(M):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append((v, w))
    G[v + N].append((u + N, w))
for i in range(N):
    G[i].append((i + N, 0))

dist = [float("inf")] * (2 * N)
visited = [False] * (2 * N)
dist[0] = 0
heap = [(0, 0)]

while heap:
    d, v = heappop(heap)
    if visited[v]:
        continue
    visited[v] = True
    for ch, w in G[v]:
        new_d = d + w
        if new_d < dist[ch]:
            dist[ch] = new_d
            heappush(heap, (new_d, ch))

for i in range(N + 1, 2 * N):
    if dist[i] == float("inf"):
        print("-1", end=" ")
    else:
        print(dist[i], end=" ")
