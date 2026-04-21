class UnionFind:
    def __init__(self):
        self.root = {}
        self.size = defaultdict(lambda : 1)

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
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        # union find
        # group then distribute

        dsu = UnionFind()
        n = len(source)

        for i in range(n):
            dsu.find(i)

        for u, v in allowedSwaps:
            dsu.union(u, v)

        group = defaultdict(lambda: Counter())

        for i in range(n):
            num = source[i]

            root = dsu.find(i)

            group[root][num] += 1

        
        source = [-1 for _ in range(n)]
        rem = []
        for i in range(n):
            root = dsu.find(i)

            tar = target[i]

            if group[root][tar] > 0:
                source[i] = tar
                group[root][tar] -= 1

                if group[root][tar] == 0:
                    del group[root][tar]

            else:
                rem.append(i)



        diff = 0
        for i in range(n):
            if source[i] != target[i]:
                diff += 1

        return diff        
