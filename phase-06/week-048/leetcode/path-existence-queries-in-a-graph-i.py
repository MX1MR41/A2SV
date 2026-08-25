class UnionFind:
    def __init__(self, n):
        self.root = {node:node for node in range(n)}
        self.rank = defaultdict(int)

    def find(self, x):
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
            self.root[rooty] = rootx
            self.rank[rootx] += 1


class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:

        nodes = [(i, nums[i]) for i in range(n)]
        nodes.sort(key = lambda x: [x[1], x[0]])

        dsu = UnionFind(n)

        for i in range(n - 1):
            node1, val1 = nodes[i]
            node2, val2 = nodes[i + 1]
            if val2 - val1 <= maxDiff:
                dsu.union(node1, node2)

        res = []
        for node1, node2 in queries:
            if dsu.find(node1) == dsu.find(node2):
                res.append(True)
            else:
                res.append(False)

        return res


        
