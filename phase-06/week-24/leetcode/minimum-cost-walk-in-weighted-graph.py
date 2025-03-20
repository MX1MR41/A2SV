class UnionFind:
    def __init__(self):
        self.root = dict()
        self.rank = defaultdict(int)

    def find(self, x):
        if x not in self.root:
            self.root[x] = x
            return x

        while self.root[x] != x:
            x = self.root[x]
            self.root[x] = self.root[self.root[x]]

        return self.root[x]

    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx != rooty:
            rankx, ranky = self.rank[rootx], self.root[rooty]
            if rankx > ranky:
                self.root[rooty] = rootx
            elif rankx < ranky:
                self.root[rootx] = rooty
            else:
                self.root[rootx] = rooty
                self.rank[rooty] += 1


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        # bit manipulation + unionfind
        # give a connected component, if we want to minimize the total AND of moving from u to v,
        # we can traverse through all the edges because the more you AND a new weight, the smaller
        # the cumulative AND gets.
        # so first create a dsu with the given edges, then for every connected component,
        # minimize the total AND by accumulating every edge via AND-ing them together
        
        dsu = UnionFind()
        for u, v, w in edges:
            dsu.union(u, v)

        total_and = dict()

        for u, v, w in edges:
            root = dsu.find(u)
            if root not in total_and:
                total_and[root] = w
            else:
                total_and[root] &= w

        res = []
        for u, v in query:
            if dsu.find(u) != dsu.find(v):
                res.append(-1)
            else:
                root = dsu.find(u)
                res.append(total_and[root])


        return res

        
