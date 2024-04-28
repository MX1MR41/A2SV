from collections import defaultdict


def bfs(u):
    visited.add(u)
    stk = []
    stk.append(u)
    while stk:
        vertex = stk.pop()
        if len(graph[vertex]) != 2:
            global cyc
            cyc = 0

        for i in graph[vertex]:
            if i not in visited:
                visited.add(i)
                stk.append(i)


n, m = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

components = 0
visited = set()


for node in range(1, n + 1):
    cyc = 1
    if node not in visited:
        bfs(node)
        if cyc == 1:
            components += 1

print(components)
