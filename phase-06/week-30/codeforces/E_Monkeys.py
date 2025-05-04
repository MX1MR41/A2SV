# https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/E

from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.root = {i: i for i in range(1, n + 1)}
        self.rank = defaultdict(int)
        self.fall_time = defaultdict(lambda : -1)


    def find(self, x):

        if self.root[x] == x:
            return x, self.fall_time[x]

        rootx, max_time = self.find(self.root[x])
        self.fall_time[x] = max(self.fall_time[x], max_time)
        
        self.root[x] = rootx

        return rootx, self.fall_time[x]


    def union(self, x, y, t):
        rootx, _ = self.find(x)
        rooty, _ = self.find(y)

        if rootx == rooty:
            return 
        

        if rootx == 1:
            self.root[rooty] = 1
            self.fall_time[rooty] = t

        elif rooty == 1:
            self.root[rootx] = rooty
            self.fall_time[rootx] = t

        else:

            rankx, ranky = self.rank[rootx], self.rank[rooty]

            if rankx < ranky:
                self.root[rootx] = rooty
                self.fall_time[rooty] = max(self.fall_time[rooty], self.fall_time[rootx])
                
            elif rankx > ranky:
                self.root[rooty] = rootx
                self.fall_time[rootx] = max(self.fall_time[rooty], self.fall_time[rootx])

            else:
                self.root[rooty] = rootx
                self.rank[rootx] += 1
                self.fall_time[rooty] = max(self.fall_time[rooty], self.fall_time[rootx])




n, m = list(map(int, input().split()))


hands = [[-1, -1] for _ in range(n + 1)]


for i in range(n):
    left, right = list(map(int, input().split()))
    hands[i + 1] = [left, right]

removed = []
set_removed = set()

for _ in range(m):
    monkey, hand = list(map(int, input().split()))

    removed.append((monkey, hand))
    set_removed.add((monkey, hand))

dsu = UnionFind(n)

for mon in range(1, n + 1):
    left, right = hands[mon]

    if left != -1 and (mon, 1) not in set_removed:
        dsu.union(mon, left, -1)

    if right != -1 and (mon, 2) not in set_removed:
        dsu.union(mon, right, -1)
        
 
for t in range(m - 1, -1, -1):
    mon, hand = removed[t]
    next_mon = hands[mon][hand - 1]
    dsu.union(mon, next_mon, t)


res = [-1] * (n + 1)
for i in range(2, n + 1):
    _, fall_time = dsu.find(i)
    res[i] = fall_time

for i in range(1, n + 1):
    print(res[i])




