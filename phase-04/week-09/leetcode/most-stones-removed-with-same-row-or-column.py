class UnionFind:
    def __init__(self, n):
        self.root = {i:i for i in range(n)}
        self.rank = defaultdict(int)
        self.len = {i:1 for i in range(n)}

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])

        return self.root[x]

    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        rankx, ranky = self.rank[rootx], self.rank[rooty]
        lenx, leny = self.len[rootx], self.len[rooty]

        if rootx != rooty:
            if rankx < ranky:
                self.root[rootx] = rooty
            elif rankx > ranky:
                self.root[rooty] = rootx
            else:
                self.root[rootx] = rooty
                self.rank[rooty] += 1

            self.len[rootx] = self.len[rooty] = lenx + leny



class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # we use unionfind to group stones which share either the same row or the same column
        # with any one or more stones in the same group
        # then from each group we can remove alll stones except 1, so we iterate over the groups
        # and remove (number of stones in that group - 1) stones
        n = len(stones)

        dsu = UnionFind(n)

        for i in range(n):
            for j in range(n):
                if i == j: continue

                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    dsu.union(i, j)


        ans = 0
        roots = set()
        for i in range(n):
            roots.add(dsu.find(i))


        return sum(count - 1 for count in [dsu.len[i] for i in roots])
        
