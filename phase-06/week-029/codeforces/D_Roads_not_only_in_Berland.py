# https://codeforces.com/problemset/problem/25/D

from collections import defaultdict


class UnionFind:
    def __init__(self):
        self.root = dict()
        self.rank = defaultdict(int)

    def find(self, X):
        if X not in self.root:
            self.root[X] = X
            return X

        while X != self.root[X]:
            self.root[X] = self.root[self.root[X]]
            X = self.root[X]

        return self.root[X]

    def union(self, X, Y):
        rootX, rootY = self.find(X), self.find(Y)

        if rootX != rootY:
            rankX, rankY = self.rank[rootX], self.rank[rootY]

            if rankX > rankY:
                self.root[rootY] = rootX

            elif rankX < rankY:
                self.root[rootX] = rootY

            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1


n = int(input())
roads = [list(map(int, input().split())) for _ in range(n - 1)]

dsu = UnionFind()


removed = []

for u, v in roads:

    if dsu.find(u) == dsu.find(v):
        removed.append((u, v))
    else:

        dsu.union(u, v)


added = []


for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if dsu.find(i) != dsu.find(j):
            added.append((i, j))
            dsu.union(i, j)


print(len(removed))

while removed and added:
    u, v = removed.pop()
    x, y = added.pop()

    print(u, v, x, y)
