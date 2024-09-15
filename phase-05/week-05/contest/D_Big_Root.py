from collections import defaultdict, deque

for _ in range(int(input())):
    n = int(input())
    vals = list(map(int, input().split()))
    min_vals = [float("inf")] * n
    g = defaultdict(list)
    deg = [0] * n

    ans = vals[0]
    vals[0] = float("inf")

    for i, each in enumerate(map(int, input().split())):
        g[i + 1].append(each - 1)
        deg[each - 1] += 1

    queue = deque()
    for i in range(n):
        if deg[i] == 0:
            queue.append((i, vals[i]))

    while queue:
        node, val = queue.popleft()
        if node == 0:
            break
        for neib in g[node]:
            deg[neib] -= 1
            min_vals[neib] = min(min_vals[neib], val)

            if deg[neib] == 0:
                if neib == 0:
                    vals[neib] = min(vals[neib], min_vals[neib])
                else:
                    if min_vals[neib] < vals[neib]:
                        vals[neib] = min_vals[neib]
                    else:
                        vals[neib] = (vals[neib] + min_vals[neib]) // 2
                queue.append((neib, vals[neib]))

    print(ans + vals[0])
