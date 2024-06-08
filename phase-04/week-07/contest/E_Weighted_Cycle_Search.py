"""

https://codeforces.com/gym/520688/problem/E

"""

from collections import defaultdict
from sys import stdin


def input(): return stdin.readline().strip()

class DSU:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, v):
        while v != self.p[v]:
            self.p[v] = self.p[self.p[v]]
            v = self.p[v]
        return v
    
    def merge(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.size[pu] < self.size[pv]:
            pu, pv = pv, pu
        self.size[pu] += self.size[pv]
        self.p[pv] = pu
        return True

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    edges = []
    adj = defaultdict(list)
    for __ in range(M):
        u, v, w = map(int, input().split())
        u, v = u - 1, v - 1
        edges.append((w, u, v))
        adj[u].append(v)
        adj[v].append(u)

    edges.sort(key=lambda edge: edge[0], reverse=True)
    dsu = DSU(N)
    for w, u, v in edges:
        if not dsu.merge(u, v):
            ans = (w, u, v)

    min_w, st, end = ans
    stk = [st]


    # DFS to get the cycle
    p = [-1]*N
    p[st] = st
    while stk:
        v = stk.pop()
        for ch in adj[v]:
            if v == st and ch == end: continue
            if ch == end:
                p[ch] = v
                stk = []
                break
            if p[ch] == -1:
                p[ch] = v
                stk.append(ch)
    v = end
    path = []
    while p[v] != v:
        path.append(v)
        v = p[v]
    path.append(st)

    print(min_w, len(path))
    for i in range(len(path)):
        path[i] += 1
    print(*path)