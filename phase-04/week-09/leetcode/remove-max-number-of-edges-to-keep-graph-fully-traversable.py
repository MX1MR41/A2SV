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

            return True # adding this edge won't create a cycle

        else: return False # adding this edge will create a cycle


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # unionfind coupled with kruskal's algorithm
        # we try to minimize the total number of edges by first connecting
        # the type 3 path's since they are traversable by both Alice and Bob
        # hence, we store the edges in a heap where all the type 3 edges come first
        edges = [[-edge[0], edge[1], edge[2]] for edge in edges]
        heapify(edges)

        # we need two to represent the traversing options of both Alice and Bob 
        bob = UnionFind(n)
        alice = UnionFind(n)

        res = 0

        while edges:
            curr = heappop(edges)
            path, u, v = -curr[0], curr[1], curr[2]
            if path == 3: # traversable by both so we union for both
                a, b = alice.union(u, v), bob.union(u, v)
                # if adding this edge for either will cause a cycle,
                # we (implicitly) remove the edge that was added for only one of them
                if not a or not b: 
                    res += 1

            elif path == 2:
                b = bob.union(u,v)
                if not b: # causee a cycle, hence removable
                    res += 1
            else:
                a = alice.union(u,v)
                if not a:
                    res += 1

        totA = set(alice.find(i) for i in range(1, n+1))
        totB = set(bob.find(i) for i in range(1, n+1))
        # if the number of connected components for either is greater than 1
        # even with all edges exhausted, it is impossible to create full path for both
        if len(totA) > 1 or len(totB) > 1:
            return -1 


        return res
        
