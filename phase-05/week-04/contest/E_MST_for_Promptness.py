"""

https://codeforces.com/gym/544854/problem/E

"""

from collections import defaultdict, deque



N, M = map(int, input().split())

adj = defaultdict(set)
for _ in range(M):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    adj[u].add(v)
    adj[v].add(u)

unconnected = set(range(N))
edges = 0

for i in range(N):
    if i in unconnected:
        q = deque([i])
        unconnected.remove(i)
        while q:
            v = q.popleft()
            remove = []
            for u in unconnected:
                if v not in adj[u]:
                    edges += 1
                    remove.append(u)
                    q.append(u)
            for u in remove:
                unconnected.remove(u)
print(N - 1 - edges)