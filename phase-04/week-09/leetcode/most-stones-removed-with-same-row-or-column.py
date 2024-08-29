class UnionFind:
    def __init__(self, arr):
        self.root = {tuple(a):tuple(a) for a in arr}
        self.rank = defaultdict(int)

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])

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
                self.root[rootx] = rooty
                self.rank[rooty] += 1

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # we use unionfind to group stones which share either the same row or the same column
        # with any one or more stones in the same group
        # then from each group we can remove all stones except 1, so we iterate over the groups
        # and remove (number of stones in that group - 1) stones
        dsu = UnionFind(stones)
        n = len(stones)
        for i in range(n):
            r, c = stones[i]
            for j in range(i+1, n):
                rp, cp = stones[j]
                if r == rp or c == cp:
                    dsu.union((r,c), (rp, cp))

        groups = defaultdict(set)
        for i in stones:
            groups[dsu.find(tuple(i))].add((tuple(i)))


        ans = 0
        for s in groups.values():
            ans += len(s) - 1

        return ans
        
