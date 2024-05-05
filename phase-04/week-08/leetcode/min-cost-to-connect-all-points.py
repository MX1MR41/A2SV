class UnionFind:
    def __init__(self, n):
        self.root = {i:i for i in range(n)}
        self.rank = defaultdict(int)

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])

        return self.root[x]

    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        # x and y are already connected and adding another edge would create a cycle
        if rootx == rooty: return False

        rankx, ranky = self.rank[rootx], self.rank[rooty]
        if rankx < ranky:
            self.root[rootx] = rooty
        elif rankx > ranky:
            self.root[rooty] = rootx
        else:
            self.root[rootx] = rooty
            self.rank[rooty] += 1

        # to indicate that the addition of an edge between x and y won't create cycle
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Kruskal's algorithm. Unionfind coupled with min heap
        # enumerate all possible edges along with their weights in a heap
        # then connect the least costliest edges until we have a connected MST
        dist = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) # manhattan distance
        n = len(points)
        dsu = UnionFind(n)

        edges = []

        # create all possible edges for a complete graph
        # and push them into a heap with their respective weights
        for i in range(n):
            for j in range(i+1, n):
                curr = dist(points[i], points[j])
                heappush(edges, (curr, i, j))



        cost = num_edges = 0

        while edges:
            d, x, y = heappop(edges)
            if dsu.union(x, y): # no edge between them yet. Ensures we dont create a cycle
                cost += d
                num_edges += 1
                # all points have been connected
                if num_edges == n-1: break

        return cost

        
