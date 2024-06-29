class UnionFind:
    def __init__(self, n):
        self.root = list(range(n))
        self.rank = defaultdict(int)

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])

        return self.root[x]

    def union(self, x,y):
        rootx, rooty = self.find(x), self.find(y)

        if rootx != rooty:
            rankx, ranky = self.rank[rootx], self.rank[rooty]
            if rankx > ranky:
                self.root[rooty] = rootx
            elif rankx < ranky:
                self.root[rootx] = rooty
            else:
                self.root[rooty] = rootx
                self.rank[rootx] += 1



class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        dsu = UnionFind(n)
        for a, b in edges:
            dsu.union(a,b)

        group = defaultdict(set)
        for i in range(n):
            root = dsu.find(i)
            group[root].add(i)

        # print(group)

        ans = 0

        for root, g in group.items():
            curr = len(g)
            n -= curr
            ans += curr * n 
            

        return ans
        
