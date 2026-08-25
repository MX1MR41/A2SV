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
    def equationsPossible(self, equations: List[str]) -> bool:

        dsu = UnionFind()

        equal = []
        inequal = []
        for eq in equations:
            if eq[1:-1] == "==":
                equal.append(eq)
            else:
                inequal.append(eq)

        for eq in equal:
            dsu.union(eq[0], eq[-1])

        for eq in inequal:
            if dsu.find(eq[0]) == dsu.find(eq[-1]):
                return False

        return True
        
