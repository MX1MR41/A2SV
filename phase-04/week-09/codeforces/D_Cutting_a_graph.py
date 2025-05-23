# the key to solving the cutting part is, well there is no
# optimal approach than dfs-ing and updating roots one by one
# so instead we process the queries in reverse, and when we face a cut, we union 
# https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D

from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.root = list(range(n + 1))
        self.rank = defaultdict(int)

    def find(self, x):
        while self.root[x] != x:
            x = self.root[x]
            self.root[x] = self.root[self.root[x]]
        return self.root[x]

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

n, m, k = list(map(int, input().split()))

dsu = UnionFind(n)
for _ in range(m):
    input()

queries = []
res = []
for _ in range(k):
    queries.append(input().split())

queries.reverse()

for que in queries:
    u, v = int(que[-2]), int(que[-1])
    if "ask" in que:
        if dsu.find(u) == dsu.find(v):
            res.append("YES")
        else:
            res.append("NO")
    else:
        dsu.union(u, v)

print(*res[::-1], sep="\n")
