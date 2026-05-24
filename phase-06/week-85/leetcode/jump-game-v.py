class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        # graph, top sort
        # problem boils don to finding the longest path in a graph, 
        # which can be calculated using top sort
        g = defaultdict(list)
        deg = defaultdict(int)
        n = len(arr)
        for i in range(n):
            for j in range(i + 1, i + d + 1):
                if j >= n or arr[j] >= arr[i]:
                    break

                g[j].append(i)
                deg[i] += 1

        for i in range(n - 1, -1, -1):
            for j in range(i - 1, i - d - 1, -1):
                if j < 0 or arr[j] >= arr[i]:
                    break

                g[j].append(i)
                deg[i] += 1




        que = deque()
        for i in range(n):
            if deg[i] == 0:
                que.append(i)

        res = 0
        while que:
            for i in range(len(que)):
                i = que.popleft()

                for j in g[i]:
                    deg[j] -= 1
                    if deg[j] == 0:
                        que.append(j)

            res += 1

        return res

