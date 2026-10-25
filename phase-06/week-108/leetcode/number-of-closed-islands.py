class UnionFind:
    def __init__(self):
        self.root = {}
        self.size = defaultdict(lambda: 1)

    def find(self, x):
        if x not in self.root:
            self.root[x] = x

        while x != self.root[x]:
            self.root[x] = self.root[self.root[x]]
            x = self.root[x]

        return self.root[x]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)

        if rooty == rootx:
            return

        sizex = self.size[rootx]
        sizey = self.size[rooty]

        if sizex >= sizey:
            self.root[rooty] = rootx
            self.size[rootx] += sizey
        else:
            self.root[rootx] = rooty
            self.size[rooty] += sizex


class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:

        m, n = len(grid), len(grid[0])

        dsu = UnionFind()

        valid = lambda x, y: 0 <= x < m and 0 <= y < n
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for i in range(m):
            for j in range(n):

                if grid[i][j] == 1:
                    continue

                dsu.find((i, j))
                for di, dj in dirs:
                    ni, nj = i + di, j + dj

                    if not valid(ni, nj) or grid[ni][nj] == 1:
                        continue

                    dsu.union((i, j), (ni, nj))

        invalid = set()

        for i in range(m):
            if grid[i][0] == 0:
                invalid.add(dsu.find((i, 0)))
            if grid[i][n - 1] == 0:
                invalid.add(dsu.find((i, n - 1)))

        for j in range(n):
            if grid[0][j] == 0:
                invalid.add(dsu.find((0, j)))
            if grid[m - 1][j] == 0:
                invalid.add(dsu.find((m - 1, j)))

        final = set([dsu.find(x) for x in dsu.root if dsu.find(x) not in invalid])
        return len(final)
