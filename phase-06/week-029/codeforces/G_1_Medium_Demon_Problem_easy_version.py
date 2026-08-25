# https://codeforces.com/contest/2044/problem/G1

from collections import defaultdict, deque


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    g = defaultdict(list)
    indeg = defaultdict(int)

    for i in range(n):
        g[i + 1].append(arr[i])

        indeg[arr[i]] += 1

    res = 1

    que = deque()

    for i in range(1, n + 1):
        if indeg[i] == 0:
            que.append(i)

    while que:
        res += 1
        for _ in range(len(que)):
            node = que.popleft()

            for nei in g[node]:
                indeg[nei] -= 1

                if indeg[nei] == 0:
                    que.append(nei)


    print(res + 1)
