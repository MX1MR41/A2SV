class UnionFind:
    def __init__(self, n):
        self.root = {i:i for i in range(1, n+1)}
        self.rank = defaultdict(int)

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])

        return self.root[x]

    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx != rooty: 
            rankx, ranky = self.rank[rootx], self.rank[rooty]
            if rankx < ranky:
                self.root[rootx] = rooty
            elif rankx > ranky:
                self.root[rooty] = rootx
            else:
                self.root[rootx] = rooty
                self.rank[rooty] += 1

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # use unionfind to find all the cities that are connected to each other
        # then find the minimum from the group in which 1 and n belong to

        dsu = UnionFind(n)

        for x, y, dist in roads:
            dsu.union(x,y)

        root = dsu.find(1)

        connected = set()
        for i in range(1, n+1):
            if dsu.find(i) == root:
                connected.add(i)

        minimum = float("inf")
        for x, y, dist in roads:
            if x in connected and y in connected:
                minimum = min(minimum, dist)
                

        return minimum
        
