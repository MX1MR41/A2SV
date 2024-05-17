"""

https://codeforces.com/gym/515998/problem/D

PASSED
"""

import sys
from collections import defaultdict
n = int(sys.stdin.readline().strip())
graph = defaultdict(list)

for i in range(n - 1):
    u, v = map(int, sys.stdin.readline().strip().split())
    graph[u].append(v)
    graph[v].append(u)
init = list(map(int, sys.stdin.readline().strip().split()))
goal = list(map(int, sys.stdin.readline().strip().split()))
stack = [(1, 1, 0, 0, 0)]
ans = []

while stack:
    node, par, level, even_op, odd_op = stack.pop()
    if level % 2 == 0:
        if even_op % 2:
            if 1 - init[node - 1] != goal[node - 1]:
                ans.append(node)
                even_op = 1 -even_op
        else:
            if init[node - 1] != goal[node - 1]:
                ans.append(node)
                even_op = 1 -even_op
    else:
        if odd_op % 2:
            if 1 - init[node - 1] != goal[node - 1]:
                ans.append(node)
                odd_op = 1 -odd_op
        else:
            if init[node - 1] != goal[node - 1]:
                ans.append(node)
                odd_op = 1 -odd_op
    for el in graph[node]:
        if el != par:
            stack.append((el, node, level + 1, even_op, odd_op))
print(len(ans))
for a in ans:
    print(a)