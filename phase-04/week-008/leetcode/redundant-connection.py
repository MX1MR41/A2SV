class UnionFind:
    def __init__(self, size):
        self.root = {i: i for i in range(1, size + 1)}
        self.rank = [0] * (size + 1)

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x]) 
        return self.root[x]



    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        rankx, ranky = self.rank[rootx], self.rank[rooty]

        if rootx != rooty:
            if rankx > ranky:
                self.root[rooty] = rootx
            elif rankx < ranky:
                self.root[rootx] = rooty
            else:
                self.root[rootx] = rooty
                self.rank[rootx] += 1
            

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # if two nodes are in the same set, then unionizing them is redundant
        n = len(edges)
        dsu = UnionFind(n)

        for i in range(n):

            u, v = edges[i]
            
            rootu, rootv = dsu.find(u), dsu.find(v)

            if rootu == rootv:
                return edges[i]

            dsu.union(u,v)

        return edges[-1]

