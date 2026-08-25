# https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/C

from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.root = {i: i for i in range(1, n + 1)}
        self.rank = defaultdict(int)
        self.xp = defaultdict(int) # total xp of each player 
        self.offset = defaultdict(int) # offset to keep track of the undeserved xp's a player gets

    def find(self, x):
        # we move up the tree to the root while accumulating the xp's and offsets of all nodes
        # except the root node. After path compression, all nodes will point directly to the root
        # so to get the total xp of a player we will add the root's xp into the players then deduct the player's offset.

        if self.root[x] == x:
            # we return 0 for both xp and offset so that we don't accumulate a root's xp
            # and offset to a child
            return x, 0, 0

        rootx, totxp, netoffset = self.find(self.root[x])

        # accumulate and compress path
        self.xp[x] += totxp
        self.offset[x] += netoffset
        self.root[x] = rootx

        return rootx, self.xp[x], self.offset[x]

    def union(self, x, y):
        rootx, _, _ = self.find(x)
        rooty, _, _ = self.find(y)

        if rootx == rooty:
            return

        rankx, ranky = self.rank[rootx], self.rank[rooty]
        if rankx > ranky:
            self.root[rooty] = rootx
            # add the larger tree's xp as an offset to the smaller tree because we don't
            # want the smaller tree to get undeserved xp. 
            # We don't need to accumulate the larger tree's offset tho, cuz we're attaching it to a root
            # and a root's offset is zero, until it gets merged into another tree
            self.offset[rooty] += self.xp[rootx]

        elif rankx < ranky:
            self.root[rootx] = rooty
            self.offset[rootx] += self.xp[rooty]

        else:
            self.root[rootx] = rooty
            self.offset[rootx] += self.xp[rooty]
            self.rank[rooty] += 1

    def getxp(self, x):

        rootx, _, _ = self.find(x)

        if rootx != x:
            # since the path will be compressed, the node will point directly to the root 
            # and it will have accumulated the xps and offsets of all its ancestors except the root's
            # so to compute x's xp, we add the root's xp to x's xp and we deduct x's offset.
            # we don't really need to deduct the root's offset from the answer because if a node is a root,
            # its offset will always be zero, until it gets merged into another tree
            return self.xp[rootx] + self.xp[x] - self.offset[x]
        
        else:
            return self.xp[x] - self.offset[x]


    def addxp(self, x, xp):
        rootx, _, _ = self.find(x)
        self.xp[rootx] += xp


n, q = list(map(int, input().split()))

dsu = UnionFind(n)
for _ in range(q):
    query = list(input().split())
    if query[0] == "add":
        dsu.addxp(int(query[1]), int(query[2]))

    elif query[0] == "join":
        dsu.union(int(query[1]), int(query[2]))

    else:
        xp = dsu.getxp(int(query[1]))
        print(xp)
