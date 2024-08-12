class UnionFind:
    def __init__(self):
        self.root = dict()
        self.rank = defaultdict(int)

    def find(self, x):
        if x not in self.root:
            self.root[x] = x
            return x

        if x != self.root[x]:
            self.root[x] = self.find(self.root[x]) 

        return self.root[x]

    def union(self, x, y):
        nonlocal regions
        rootx, rooty = self.find(x), self.find(y)
        if rootx != rooty:
            regions -= 1
            rankx, ranky = self.rank[rootx], self.rank[rooty]
            if rankx < ranky:
                self.root[rootx] = rooty
            elif rankx > ranky:
                self.root[rooty] = rootx
            else:
                self.root[rootx] = rooty
                self.rank[rooty] += 1


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        dsu = UnionFind()
        regions = 4 * n * n

        for r in range(n):
            for c in range(n):
                curr = grid[r][c]
                if curr == " ":
                    dsu.union(f"{r}{c}u", f"{r}{c}l")
                    dsu.union(f"{r}{c}l", f"{r}{c}d")
                    dsu.union(f"{r}{c}d", f"{r}{c}r")

                elif curr == "\\":
                    dsu.union(f"{r}{c}r", f"{r}{c}u")
                    dsu.union(f"{r}{c}l", f"{r}{c}d")
                
                elif curr == "/":
                    dsu.union(f"{r}{c}u", f"{r}{c}l")
                    dsu.union(f"{r}{c}d", f"{r}{c}r")

                if 0 <= r - 1 < n:
                    dsu.union(f"{r}{c}u", f"{r - 1}{c}d")
                if 0 <= r + 1 < n:
                    dsu.union(f"{r}{c}d", f"{r + 1}{c}u")
                if 0 <= c - 1 < n:
                    dsu.union(f"{r}{c}l", f"{r}{c - 1}r")
                if 0 <= c + 1 < n:
                    dsu.union(f"{r}{c}r", f"{r}{c + 1}l")


        return regions
