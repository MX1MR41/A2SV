# https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/C

from collections import defaultdict


class UnionFind:
    def __init__(self, n_max_players):

        self.root = {i: i for i in range(1, n_max_players + 1)}
        self.rank = defaultdict(int)
        self.xp = defaultdict(int)
        self.offset = defaultdict(int)

    def find(self, i):
        if self.root[i] == i:
            return i

        original_parent = self.root[i]
        true_root = self.find(original_parent)

        self.offset[i] += self.offset[original_parent]

        self.root[i] = true_root
        return true_root

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx == rooty:
            return

        if self.rank[rootx] < self.rank[rooty]:

            self.root[rootx] = rooty

            self.offset[rootx] = self.xp[rootx] - self.xp[rooty]
        elif self.rank[rootx] > self.rank[rooty]:

            self.root[rooty] = rootx
            self.offset[rooty] = self.xp[rooty] - self.xp[rootx]
        else:

            self.root[rooty] = rootx
            self.offset[rooty] = self.xp[rooty] - self.xp[rootx]
            self.rank[rootx] += 1

    def getxp(self, x):
        root_of_x = self.find(x)

        return self.xp[root_of_x] + self.offset[x]

    def addxp(self, x, value_v):
        root_of_x = self.find(x)

        self.xp[root_of_x] += value_v



n_players, m_queries = map(int, input().split())

dsu = UnionFind(n_players)

results_to_print = []

for _ in range(m_queries):
    query_parts = input().split()
    command = query_parts[0]

    if command == "add":
        player_x_id = int(query_parts[1])
        value_v = int(query_parts[2])
        dsu.addxp(player_x_id, value_v)
    elif command == "join":
        player_x_id = int(query_parts[1])
        player_y_id = int(query_parts[2])
        dsu.union(player_x_id, player_y_id)
    else:
        player_x_id = int(query_parts[1])
        exp = dsu.getxp(player_x_id)
        results_to_print.append(str(exp))

print("\n".join(results_to_print) + "\n")
