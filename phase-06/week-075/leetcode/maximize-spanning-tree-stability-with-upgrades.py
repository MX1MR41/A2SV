class UnionFind:
    def __init__(self):
        self.root = {}
        self.size = defaultdict(lambda: 1)

    def find(self, x):
        if x not in self.root:
            self.root[x] = x

        while x != self.root[x]:
            self.root[x] = self.root[self.root[x]]
            x = self.root[x]

        return self.root[x]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx == rooty:
            return

        sizex = self.size[rootx]
        sizey = self.size[rooty]

        if sizex >= sizey:
            self.root[rooty] = rootx
            self.size[rootx] += sizey
        else:
            self.root[rootx] = rooty
            self.size[rooty] += sizex


class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        # union find + heap
        # connect the edges that must be connected first and connect them
        # then for the remaining edges, group them by the components that they connect
        # i.e. all edges that connect components A and B should be grouped together
        # and from each such group we will choose only one, and that will be the one with
        # the highest strength


        dsu = UnionFind()

        res = float("inf")
        for u, v, s, m in edges:
            if m == 1:
                rootu = dsu.find(u)
                rootv = dsu.find(v)

                if rootu == rootv: # a cycle is inevitable so return -1
                    return -1

                dsu.union(u, v)

                res = min(res, s)


        grouped = defaultdict(lambda: [0, 0, 0]) # [u, v, s]

        for u, v, s, m in edges:
            if m == 1:
                continue

            rootu = dsu.find(u)
            rootv = dsu.find(v)

            if rootu == rootv:
                continue

            group = grouped[(min(rootu, rootv), max(rootu, rootv))]

            if s > group[2]: # a stronger edge found for this group
                group[0] = u
                group[1] = v
                group[2] = s

        listed = list(grouped.values())

        # connect the strongest edges first to maximize stability
        listed.sort(key=lambda x: x[-1], reverse=True)

        heap = []
        for u, v, s in listed:
            rootu = dsu.find(u)
            rootv = dsu.find(v)
            if rootu == rootv:
                continue

            dsu.union(u, v)

            # keep track of the upgradable edges in a weakest-first order
            heappush(heap, s)

        while heap and k:
            s = heappop(heap)
            res = min(res, 2 * s) # upgrade edge and compare with the minimum so far
            k -= 1

        if heap:
            res = min(res, heap[0])


        # check if the whole network is connected
        root = dsu.find(0)
        for u in range(n):
            rootu = dsu.find(u)
            if rootu != root:
                return -1

        return res
