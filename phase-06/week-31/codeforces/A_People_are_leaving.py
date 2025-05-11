# https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/A

class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n + 1)]

        self.next = {i: i for i in range(n + 1)}
        self.next[-1] = -1

    def find(self, x):
        while x != self.root[x]:
            self.root[x] = self.root[self.root[x]]
            x = self.root[x]

        return self.root[x]

    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)

        if rootx == rooty:
            return

        if rootx > rooty:
            self.root[rooty] = rootx
        else:
            self.root[rootx] = rooty

    def findnext(self, x):

        nextx = x
        while self.next[nextx] != nextx:
            nextx = self.next[nextx]

        while x != -1 and x != self.next[x]:

            parent = self.next[x]
            self.next[x] = nextx
            x = parent

        return nextx


n, q = list(map(int, input().split()))

dsu = UnionFind(n)

for _ in range(q):
    que = list(input().split())
    x = int(que[1])
    if que[0] == "-":
        if x == n:
            dsu.next[n] = -1
        else:
            dsu.next[x] = dsu.next[x + 1]
            dsu.union(x, x + 1)
    else:
        res = dsu.findnext(x)
        print(res)
