class UnionFind:
    def __init__(self):
        self.root = dict()
        self.rank = defaultdict(int)

    def find(self, x):
        if x not in self.root:
            self.root[x] = x
            return x

        while x != self.root[x]:
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

            



class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dsu = UnionFind()
        inbound = lambda i, j: 0 <= i < n and 0 <= j < n
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    for di, dj in dirs:
                        ni, nj = i + di, j + dj
                        if inbound(ni, nj) and grid[ni][nj]:
                            dsu.union((i, j), (ni, nj))

        vals = defaultdict(int)
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    vals[dsu.find((i, j))] += 1

        res = max(vals.values()) if vals.values() else 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    temp = 0
                    seen = set()
                    for di, dj in dirs:
                        ni, nj = i + di, j + dj
                        if inbound(ni, nj) and grid[ni][nj]:
                            root = dsu.find((ni, nj))
                            if root not in seen:
                                temp += vals[root]
                                seen.add(root)

                    res = max(res, temp + 1)

        return res


                
        
