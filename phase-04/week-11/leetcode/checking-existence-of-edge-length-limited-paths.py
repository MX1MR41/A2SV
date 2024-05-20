class UnionFind:
    def __init__(self, n):
        self.root = list(range(n))
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
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # unionfind + heap + sorting
        # we restructure the edgeList into a heap sorted by the length of edge
        # we sort the queries by their limit, then when iterating through the sorted
        # queries, we form all edges whose length is less than the limit. 
        # If after doing that the two nodes are connected, 
        # then the answer fro that query is True
        dsu = UnionFind(n)
        
        ans = [0] * len(queries)
        edges = [edge[::-1] for edge in edgeList]
        heapify(edges)

        for ind, que in enumerate(queries):
            queries[ind] = que[::-1] + [ind]

        queries.sort()

        for dist, u, v, ind in queries:
            while edges and edges[0][0] < dist:
                d, x, y = heappop(edges)
                dsu.union(x,y)

            if dsu.find(u) == dsu.find(v):
                ans[ind] = True
            else:
                ans[ind] = False

        return ans

