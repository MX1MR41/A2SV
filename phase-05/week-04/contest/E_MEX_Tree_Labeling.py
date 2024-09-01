"""

https://codeforces.com/gym/544853/problem/E

"""

import sys
from collections import defaultdict

graph = defaultdict(list)
ans = {}

n = int(sys.stdin.readline().strip())

for i in range(1, n):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(i)
    graph[b].append(i)
    ans[i] = -1

# Find the node with the maximum degree
mx = (0, 0)
for i in range(1, n + 1):
    if len(graph[i]) > mx[0]:
        mx = (len(graph[i]), i)

cur = 0
for i in graph[mx[1]]:
    ans[i] = cur
    cur += 1

for i in range(1, n):
    if ans[i] == -1:
        ans[i] = cur
        cur += 1
    print(ans[i])