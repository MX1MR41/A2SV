from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n+1)]
        self.rank = defaultdict(int)

    def find(self, x):
        while x != self.root[x]:
            self.root[x] = self.root[self.root[x]]
            x = self.root[x]

        return x
    
    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx != rooty:
            rankx, ranky = self.rank[rootx], self.rank[rooty]
            if rankx < ranky:
                self.root[rootx] = rooty
            elif rankx > ranky:
                self.root[rooty] = rootx
            else:
                self.root[rooty] = rootx
                self.rank[rootx] += 1


def span(edges, n):
    dsu = UnionFind(n)
    tot = 0
    for w, u, v in edges:
        if dsu.find(u) != dsu.find(v):
            tot |= w
            dsu.union(u, v)

    return tot

for _ in range(int(input())):
    input()
    g = defaultdict(list)
    n, m = list(map(int, input().split()))
    edges = []
    for _ in range(m):
        u, v, w = list(map(int, input().split()))
        edges.append((w,u,v))

    edges.sort()
    dsu = UnionFind(n)
    ans = float("inf")
    for i in reversed(range(32)):
        temp = [e for e in edges if not e[0] & 1 << i]
        ans = min(ans, span(temp, n))


    print(ans)


    
    