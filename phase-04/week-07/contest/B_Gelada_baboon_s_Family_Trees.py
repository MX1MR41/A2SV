"""

https://codeforces.com/gym/520688/problem/B

"""

from collections import defaultdict
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.size = [1] * size

    def find(self, x):
        while x != self.root[x]:
            self.root[x] = self.root[self.root[x]]
            x = self.root[x]
        return x
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.size[rootX] > self.size[rootY]:
                self.root[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            else:
                self.root[rootX] = rootY
                self.size[rootY] += self.size[rootX]



n = int(input())
seq = list(map(int, input().split()))
forest  = UnionFind(n)
for i in range(n):
    forest.union(i, seq[i] - 1)

tree_numbers = set()
for i in range(n):
    tree_numbers.add(forest.find(i))

print(len(tree_numbers))
