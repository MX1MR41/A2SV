from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.root = {i:i for i in range(1, n + 1)}
        self.rank = defaultdict(int)
        self.fall_time = defaultdict(lambda : -1) # track fall-time


    def find(self, x):
        # move up the tree and find the single non-negative fall-time of the group that x belongs to
        # assign the single non-negative fall-time that we found as the fall-time of all its children
        # and compress the path

        if self.root[x] == x:
            return x, self.fall_time[x]
        
        rootx, max_time = self.find(self.root[x])

        self.root[x] = rootx
        self.fall_time[x] = max(self.fall_time[x], max_time)

        return self.root[x], self.fall_time[x]
    
    def union(self, x, y, time):
        rootx, _ = self.find(x)
        rooty, _ = self.find(y)

        if rootx == rooty:
            return
        
        # make sure that monkey 1 is always the root of its group, so merging will always
        # happen into monkey 1's group. Assign the fall time of the smaller tree as the time the union happened
        if rootx == 1:
            self.root[rooty] = rootx
            self.fall_time[rooty] = time

        elif rooty == 1:
            self.root[rootx] = rooty
            self.fall_time[rootx] = time


        else:
            rankx, ranky = self.rank[rootx], self.rank[rooty]
            if rankx > ranky:
                self.root[rooty] = rootx
            elif rankx < ranky:
                self.root[rootx] = rooty
            else:
                self.root[rootx] = rooty
                self.rank[rooty] += 1




n, m = list(map(int, input().split()))

hands = [[-1, -1] for _ in range(n + 1)]


for i in range(1, n + 1):
    left, right = list(map(int, input().split()))
    hands[i] = [left, right]


removed = []
set_removed = set()

for _ in range(m):
    mon, hand = list(map(int, input().split()))

    removed.append((mon, hand))
    set_removed.add((mon, hand))



dsu = UnionFind(n)


# connect the edges that won't be removed
for mon in range(1, n+1):
    left, right = hands[mon]

    if left != -1 and (mon, 1) not in set_removed:
        dsu.union(mon, left, -1)

    if right != -1 and (mon, 2) not in set_removed:
        dsu.union(mon, right, -1)

# travel back in time and connect edges that were removed
for t in range(m - 1, -1, -1):
    mon, hand = removed[t]
    next_mon = hands[mon][hand - 1]
    dsu.union(mon, next_mon, t)

for i in range(1, n+1):
    root, fall_time = dsu.find(i)
    print(fall_time)





