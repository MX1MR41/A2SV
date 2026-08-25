# using union find
# __init__ initilizes an array root where array[i] is i's ancestral root (set representative)
# and rank[i] holds the height of the set represented by i
# find(x) returns the representative of the set that x belongs to while also compressing the path
# union(x,y) unions the sets that x and y belong to 
# and if they have the same rank, we add +1 to one of the ranks

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x]) 
        return self.root[x]



    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        rankx, ranky = self.rank[rootx], self.rank[rooty]

        if rootx != rooty:
            if rankx > ranky:
                self.root[rooty] = rootx
            elif rankx < ranky:
                self.root[rootx] = rooty
            else:
                self.root[rootx] = rooty
                self.rank[rootx] += 1



class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        dsu = UnionFind(N)

        for i in range(N):
            for j in range(N):
                if i == j: continue

                if isConnected[i][j]:
                    dsu.union(i,j)



        return len(set([dsu.find(i) for i in range(N)]))

                
        
        
