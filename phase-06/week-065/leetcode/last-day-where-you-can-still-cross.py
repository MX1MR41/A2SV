class UnionFind:
    def __init__(self):
        self.root = {}
        self.rank = defaultdict(int)

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

        if rootx == rooty:
            return

        rankx = self.rank[rootx]
        ranky = self.rank[rooty]

        if rankx > ranky:
            self.root[rooty] = rootx
        elif rankx < ranky:
            self.root[rootx] = rooty
        else:
            self.root[rooty] = rootx
            self.rank[rootx] += 1

    

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        # union find
        # perform the operations in reverse and connect land cells to each other for each
        # land cell that gets un-flooded.
        # if at time t "top" and "bottom" get connected, return t
        for cell in cells:
            cell[0] -= 1
            cell[1] -= 1

        dsu = UnionFind()

        matrix = [[0 for _ in range(col)] for _ in range(row)]
        for i, j in cells:
            matrix[i][j] = 1

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        valid = lambda i, j: 0 <= i < row and 0 <= j < col

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 1:
                    continue

                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if valid(ni, nj) and matrix[ni][nj] == 0:
                        dsu.union((i, j), (ni, nj))

                if i == 0:
                    dsu.union((i, j), "top")

                if i == row - 1:
                    dsu.union((i, j), "bottom")

    
        n = len(cells)

        if dsu.find("top") == dsu.find("bottom"):
            return n

        for t in range(n - 1, -1, -1):


            i, j = cells[t]

            matrix[i][j] = 0

            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if valid(ni, nj) and matrix[ni][nj] == 0:
                    dsu.union((i, j), (ni, nj))

            if i == 0:
                dsu.union((i, j), "top")

            if i == row - 1:
                dsu.union((i, j), "bottom")

            if dsu.find("top") == dsu.find("bottom"):
                return t

        return 0







        
        
