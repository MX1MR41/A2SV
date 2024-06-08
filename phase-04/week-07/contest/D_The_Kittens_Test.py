"""

https://codeforces.com/gym/520688/problem/D

"""

import sys
n = int(sys.stdin.readline().strip())
parent = {}
elem = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    elem[i].append(i)
    parent[i] = i
size = [1] * (n + 1)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    par_x = find(x)
    par_y = find(y) 
    if par_x != par_y:
        if size[par_x] >  size[par_y]:
            parent[par_y] = par_x
            elem[par_x].extend(elem[par_y])
            size[par_x] += size[par_y]
        else:
            parent[par_x] = par_y
            elem[par_y].extend(elem[par_x])
            size[par_y] += size[par_x]
for _ in range(n - 1):
    x, y = map(int, sys.stdin.readline().strip().split())
    union(x, y)

print(*elem[find(1)])