from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.root = list(range(n))
        self.rank = defaultdict(int)

    def find(self, x):
        while x != self.root[x]:
            self.root[x] = self.root[self.root[x]]
            x = self.root[x]

        return x

    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx != rooty:
            rankx, ranky = self.rank[rootx], self.rank[rooty]

            if rankx < ranky:
                self.root[rootx] = rooty
            elif rankx > ranky:
                self.root[rooty] = rootx
            else:
                self.root[rootx] = rooty
                self.rank[rooty] += 1


for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    s = input()
    t = input()

    dsu = UnionFind(n)
    for i in range(n):
        inds = [i + k, i + k + 1, i - k, i - k - 1]
        for ind in inds:
            if 0 <= ind < n:
                dsu.union(i, ind)

    group = defaultdict(dict)
    # print(group)

    for i in range(n):
        y = s[i]
        root = dsu.find(i)

        if y not in group[root]:
            group[root][y] = 1
        else:
            group[root][y] += 1

    ans = True
    for i in range(n):
        x = t[i]
        root = dsu.find(i)

        if x not in group[root] or group[root][x] <= 0:
            ans = False
            break

        if x in group[root]:
            group[root][x] -= 1

    if ans:
        print("YES")
    else:
        print("NO")
