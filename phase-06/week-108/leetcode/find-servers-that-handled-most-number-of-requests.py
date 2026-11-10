class SegmentTree:
    def __init__(self, n):
        self.n = 2 ** ceil(log2(n)) if n > 1 else 1
        self.tree = [0 for _ in range(2 * self.n)]

    def updatePoint(self, ind, val):
        ind += self.n
        self.tree[ind] = val

        ind //= 2

        while ind > 0:
            self.tree[ind] = min(self.tree[2 * ind], self.tree[2 * ind + 1])
            ind //= 2

    def queryRange(self, l, r, val):
        l += self.n
        r += self.n

        left_nodes = []
        right_nodes = []

        while l <= r:
            if l % 2 == 1:
                left_nodes.append(l)
                l += 1
            if r % 2 == 0:
                right_nodes.append(r)
                r -= 1

            l //= 2
            r //= 2

        nodes = left_nodes + right_nodes[::-1]

        for node in nodes:
            if self.tree[node] <= val:

                while node < self.n:
                    if self.tree[2 * node] <= val:
                        node = 2 * node
                    else:
                        node = 2 * node + 1

                return node - self.n

        return -1


class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        served = [0 for _ in range(k)]
        tree = SegmentTree(k)

        m = len(arrival)
        for i in range(m):
            a = arrival[i]
            l = load[i]
            ind = i % k

            server = tree.queryRange(ind, k - 1, a)

            if server == -1:
                server = tree.queryRange(0, ind - 1, a)

            if server != -1:
                end = a + l
                served[server] += 1
                tree.updatePoint(server, end)

        max_served = max(served)
        return [i for i in range(k) if served[i] == max_served]
