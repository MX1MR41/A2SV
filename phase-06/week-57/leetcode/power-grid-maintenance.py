class UnionFind:
    def __init__(self):
        self.root = {}
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
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx == rooty:
            return

        rankx = self.rank[rootx]
        ranky = self.rank[rooty]

        if rankx > ranky:
            self.root[rooty] = rootx
        elif rankx < ranky:
            self.root[rootx] = rooty
        else:
            self.root[rooty] = rootx
            self.rank[rootx] += 1


class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        # union find + heap 
        # group stations of the same grid, and maintain a heap for every grid to find
        # the smallest station id. Use a set to keep track of the offline nodes and 
        # perform lazy deletion on the heap

        dsu = UnionFind()

        for u, v in connections:
            dsu.union(u, v)

        group = defaultdict(list)
        for station in range(1, c + 1):
            root = dsu.find(station)
            heappush(group[root], station)


        offline = set()

        res = []
        
        for op, station in queries:
            if op == 2:
                offline.add(station)
            else:
                if station not in offline:
                    res.append(station)
                    continue

                root = dsu.find(station)
                heap = group[root]

                while heap and heap[0] in offline:
                    heappop(heap)

                if heap:
                    res.append(heap[0])
                else:
                    res.append(-1)

        return res

        
