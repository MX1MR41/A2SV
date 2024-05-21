class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.rank = [0] * (n+1)

    def find(self, x):
        while self.parent[x]!= x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return self.parent[x]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx!= rooty:
            if self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            elif self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1

n, q = list(map(int, input().split()))
dsu = UnionFind(n)
# to avoid re-unioning already union-ed ranges, 
# the next-most disjoint set for each element
# after unioning x and y, the immediate next disjoint set to x will be
# the immediate next disjoint set of y
next = {i:i+1 for i in range(1, n+1)}

for _ in range(q):
    t, x, y = list(map(int, input().split()))
    if t == 1:
        dsu.union(x, y)
    elif t == 2:
        while x < y:
            dsu.union(x, y)
            next_x = next[x]
            next[x] = next[y]
            x = next_x

    else:
        if dsu.find(x) == dsu.find(y):
            print("YES")
        else:
            print("NO")
