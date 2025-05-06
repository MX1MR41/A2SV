class UnionFind:
    def __init__(self):
        self.root = dict()
        self.rank = defaultdict(int)

    def find(self, x):

        if x not in self.root:
            self.root[x] = x
            return x

        while x != self.root[x]:
            self.root[x] = self.root[self.root[x]]
            x = self.root[x]

        return self.root[x]

    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)

        if rootx == rooty:
            return

        rankx, ranky = self.rank[rootx], self.rank[rooty]
        if rankx > ranky:
            self.root[rooty] = rootx
        elif rankx < ranky:
            self.root[rootx] = rooty
        else:
            self.root[rootx] = rooty
            self.rank[rooty] += 1



class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        # union find
        # divide cells into 4 triangular subcells numbered 1, 2, 3, 4 in a clockwise manner
        # then perform union accordingly
        n = len(grid)

        dsu =  UnionFind()

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        inbound = lambda i, j : 0 <= i < n and 0 <= j < n

        prev = {(0, 1): 2, (0, -1): 4, (1, 0) : 3, (-1, 0): 1}
        nxt = {(0, 1): 4, (0, -1): 2, (1, 0) : 1, (-1, 0): 3}

        for i in range(n):
            for j in range(n):
                cell = grid[i][j]

                if cell == " ":
                    dsu.union((i, j, 1), (i, j, 2))
                    dsu.union((i, j, 2), (i, j, 3))
                    dsu.union((i, j, 3), (i, j, 4))
                elif cell == "/":
                    dsu.union((i, j, 1), (i, j, 4))
                    dsu.union((i, j, 2), (i, j, 3))
                else:
                    dsu.union((i, j, 1), (i, j, 2))
                    dsu.union((i, j, 3), (i, j, 4))


                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if inbound(ni, nj):
                        subcell = prev[(di, dj)]
                        neicell = nxt[(di, dj)]
                        dsu.union((i, j, subcell), (ni, nj, neicell))



        return len(set([dsu.find(i) for i in dsu.root]))

