class UnionFind:
    def __init__(self, strs):
        self.root = {s:s for s in strs}
        self.rank = defaultdict(int)

    def similar(self, x, y):
        n, m = len(x), len(y)
        if n != m: return False
        diff = 0

        for i in range(n):
            if x[i] != y[i] : 
                diff += 1
                if diff > 2: return False

        return diff == 0 or diff == 2

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])

        return self.root[x]

    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        rankx, ranky = self.rank[x], self.rank[y]

        
        if rootx != rooty:
            if rankx < ranky:
                self.root[rootx] = rooty
            elif rankx > ranky:
                self.root[rooty] = rootx
            else:
                self.root[rootx] = rooty
                self.rank[rooty] += 1


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        # classic unionfind but with an added extra root validation at the end
        # to get the correct number of roots
        n = len(strs)
        dsu = UnionFind(strs)

        for i in range(n):
            for j in range(n):
                if i == j: continue

                x, y = strs[i], strs[j]
                if dsu.similar(x,y):
                    dsu.union(x, y)


        ans = set()
        for s in strs:
            ans.add(dsu.find(s))
        return len(ans)


        
