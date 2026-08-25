# https://codeforces.com/contest/744/problem/A


from collections import defaultdict


class UnionFind:
    def __init__(self, n, ks):
        self.root = [i for i in range(n + 1)]
        self.size = [1 for i in range(n + 1)]
        self.ks = set(ks)

    def find(self, x):

        while x != self.root[x]:
            self.root[x] = self.root[self.root[x]]
            x = self.root[x]

        return self.root[x]
    
    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)

        if rootx == rooty:
            return
        
        if rootx in self.ks:
            self.root[rooty] = rootx
            self.size[rootx] += self.size[rooty]
        elif rooty in self.ks:
            self.root[rootx] = rooty
            self.size[rooty] += self.size[rootx]
        else:
        
            if self.size[rootx] >= self.size[rooty]:
                self.root[rooty] = rootx
                self.size[rootx] += self.size[rooty]
            else:
                self.root[rootx] = rooty
                self.size[rooty] += self.size[rootx]


n, m, k = list(map(int, input().split()))

ks = list(map(int, input().split()))


dsu = UnionFind(n, ks)

# edges = 0

for _ in range(m):
    u, v = list(map(int, input().split()))
    dsu.union(u, v)

for i in range(1, n + 1):
    if dsu.find(i) not in dsu.ks:
        maxsize, maxroot = 0, 1

        for j in ks:
            rootj = dsu.find(j)
            sizej = dsu.size[rootj]

            if sizej >= maxsize:
                maxsize = sizej
                maxroot = rootj

        # edges += maxsize
        dsu.union(i, maxroot)


edges = -m

sizes = defaultdict(int)

for i in range(1, n + 1):
    root = dsu.find(i)
    sizes[root] = dsu.size[root]
# print(sizes)
for root, size in sizes.items():
    edges += size * (size - 1) /2

print(int(edges))
