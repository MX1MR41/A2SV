class UnionFind:
    def __init__(self, n):
        self.root = {i: i for i in range(n)}

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx != rooty:
            if rootx == 0 or rooty == 0:
                self.root[rootx] = self.root[rooty] = 0
            else:
                self.root[rooty] = rootx


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x: x[-1])
        dsu = UnionFind(n)
        dsu.union(0, firstPerson)

        i, M = 0, len(meetings)

        while i < M:
            current = [meetings[i]]
            # same time meetings
            while i < M - 1 and meetings[i + 1][2] == meetings[i][2]:
                current.append(meetings[i + 1])
                i += 1
                continue

            for x, y, time in current:
                dsu.union(x, y)

            for x, y, time in current:
                rootx = dsu.find(x)
                if rootx != 0: # these people dont know the secret
                    dsu.root[x] = x
                    dsu.root[y] = y

            i += 1

        return [i for i in range(n) if dsu.find(i) == 0]
