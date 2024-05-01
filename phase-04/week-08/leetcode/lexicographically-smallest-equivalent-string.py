class UnionFind:
    def __init__(self):
        self.root = {chr(i):chr(i) for i in range(97, 123)}

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x]) 
        return self.root[x]

    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx != rooty:
            if rootx <= rooty:
                self.root[y] = rootx
                for i in self.root:
                    if self.root[i] == rooty:
                        self.root[i] = rootx
            else:
                self.root[x] = rooty
                for i in self.root:
                    if self.root[i] == rootx:
                        self.root[i] = rooty
            

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # we can use union find to group equivalent letters together in a set 
        # represented by the lexicographically smallest letter
    
        dsu = UnionFind()

        n = len(s1)
        for i in range(n):
            dsu.union(s1[i], s2[i])

        res = ""
        for i in baseStr:
            res += dsu.find(i)

        return res
        
