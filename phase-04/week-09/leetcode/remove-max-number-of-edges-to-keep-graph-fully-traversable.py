class UnionFind:
    def __init__(self):
        self.root = dict()
        self.rank = defaultdict(int)

    def find(self, x):
        if x not in self.root:
            self.root[x] = x
            return x

        while x != self.root[x]:
            x = self.root[x]
            self.root[x] = self.root[self.root[x]]

        return self.root[x]

    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx != rooty:
            rankx, ranky = self.rank[rootx], self.rank[rooty]

            if rankx < ranky:
                self.root[rootx] = rooty
            elif rankx > ranky:
                self.root[rooty] = rootx
            else:
                self.root[rooty] = rootx
                self.rank[rootx] += 1


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = UnionFind()
        bob = UnionFind()
        edges.sort(reverse=True)

        removed = 0

        for t, u, v in edges:
            if t == 3:
                if alice.find(u) != alice.find(v) or bob.find(u) != bob.find(u):
                    alice.union(u, v)
                    bob.union(u, v)

                else:

                    removed += 1

            elif t == 2:
                if bob.find(u) != bob.find(v):
                    bob.union(u, v)
                else:

                    removed += 1

            else:
                if alice.find(u) != alice.find(v):
                    alice.union(u, v)
                else:

                    removed += 1

        b = [bob.find(i) for i in range(1, n + 1)]
        al = [alice.find(i) for i in range(1, n + 1)]

        if (
            len(set([alice.find(i) for i in range(1, n + 1)])) != 1
            or len(set([bob.find(i) for i in range(1, n + 1)])) != 1
        ):
            return -1

        return removed
