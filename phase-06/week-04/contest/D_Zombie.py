from collections import defaultdict, deque


n, m = list(map(int, input().split()))

g = defaultdict(list)
deg = defaultdict(int)

for _ in range(m):
    u, v = list(map(int, input().split()))
    deg[u] += 1
    deg[v] += 1

    g[u].append(v)
    g[v].append(u)


que = deque()
for i in range(1, n + 1):
    if deg[i] == 1:
        que.append((i, 0))

res = defaultdict(int)
seen = set()
ans = 0
while que:
    # print("que now", que)
    for _ in range(len(que)):
        node, val = que.popleft()
        if node in seen:
            continue

        seen.add(node)

        for nei in g[node]:
            deg[nei] -= 1
            # print("node", node, "nei", nei, "res", res[nei], "deg", deg[nei])
            if deg[nei] <= 1:
                ans = max(ans, val + 1 + res[nei])
                res[nei] = max(res[nei], val + 1)
                que.append((nei, res[nei]))
            else:
                res[nei] = max(res[nei], val + 1)

    # print("que after", que)

print(ans)






