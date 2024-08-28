class UnionFind:
    def __init__(self):
        self.root = defaultdict()
        self.rank = defaultdict(int)

    def find(self, x):
        if x not in self.root: # initialize it
            self.root[x] = x
            return x
        while x != self.root[x]:
            self.root[x] = self.root[self.root[x]]
            x = self.root[x]
        return x

    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx != rooty:
            rankx, ranky = self.rank[rootx], self.rank[rooty]
            if rankx > ranky:
                self.root[rooty] = rootx
            elif rankx < ranky:
                self.root[rootx] = rooty
            else:
                self.root[rooty] = rootx
                self.rank[rootx] += 1

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # group the islands using unionfind then eliminate islands which have 0's 
        dsu = UnionFind()
        m, n = len(grid2), len(grid2[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        valid = lambda r, c: 0 <= r < m and 0 <= c < n

        for r in range(m):
            for c in range(n):
                if grid2[r][c]:
                    dsu.find((r, c)) # for initialization purpose
                    for dr, dc in dirs:
                        newr, newc = r + dr, c + dc
                        if valid(newr, newc) and grid2[newr][newc]:
                            dsu.union((r, c), (newr, newc))

        count = set(dsu.find(x) for x in dsu.root) # get the roots that represent the subislands

        for i in range(m):
            for j in range(n):
                if not grid1[i][j]: # invalid subisland therefore remove the root representing it
                    count.discard(dsu.find((i, j)))

        return len(count)
