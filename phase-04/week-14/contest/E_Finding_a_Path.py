import sys
from collections import defaultdict


def solve():

    n, a, b = map(int, sys.stdin.readline().strip().split())
    graph = defaultdict(list)

    for _ in range(n - 1):
        u, v, w = map(int, sys.stdin.readline().strip().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    pref1 = [-1] * (n + 1)
    pref1[a] = 0
    stack = [(a, -1)]

    while stack:
        node, par = stack.pop()

        for ne, w in graph[node]:
            if ne != par:
                if ne == b:
                    if w ^ pref1[node] == 0:
                        return "YES"
                    continue

                pref1[ne] = w ^ pref1[node]
                stack.append((ne, node))

    ss = set(pref1)
    pref2 = [-1] * (n + 1)
    pref2[b] = 0
    stack = [(b, -1)]

    while stack:

        node, par = stack.pop()

        for ne, w in graph[node]:

            if ne != par:

                pref2[ne] = w ^ pref2[node]

                if pref2[ne] in ss:
                    return "YES"

                stack.append((ne, node))

    return "NO"


t = int(sys.stdin.readline().strip())
for _ in range(t):
    print(solve())
