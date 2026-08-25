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
            if rankx > ranky:
                self.root[rooty] = rootx
            elif rankx < ranky:
                self.root[rootx] = rooty

            else:
                self.root[rooty] = rootx
                self.rank[rootx] += 1

        
        

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # union find
        # find connected components using union find
        # count number of nodes and number of edges of every connected component
        # if number of edges == (number of nodes)*(number of nodes - 1)/2, => it is complete
        dsu = UnionFind()
        for u, v in edges:
            dsu.union(u, v)

        num_nodes = defaultdict(int)
        for i in range(n):
            num_nodes[dsu.find(i)] += 1

        num_edges = defaultdict(int)

        for u, v in edges:
            root = dsu.find(u)
            num_edges[root] += 1


        res = 0
        for root, nodes in num_nodes.items():
            edges = num_edges[root]
            if edges == nodes*(nodes - 1)/2:
                res += 1

        return res

        
