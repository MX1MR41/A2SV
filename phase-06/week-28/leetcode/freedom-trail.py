class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        # bfs + dp
        # since the greedy approach where we try to find the closest letter fails, the solution is dp
        # for every target letter in key, we collect all the possible indices which have the 
        # target letter as candidates for bfs sources, and we compute the minimum steps to it, 
        # from all the possible sources in our bfs que

        n = len(ring)

        que = deque([(0, 0)])

        for i, k in enumerate(key):

            dp = defaultdict(lambda: float("inf"))

            candidates_indices = set()

            for _ in range(len(que)):

                ind, d = que.popleft()

                for j in range(n):

                    if ring[j] == k:
                        if j == ind:
                            new_d = d + 1
                        else:
                            new_d = d + 1 + min((abs(j - ind), min(j, ind) + (n - (max(j, ind)))))
                            

                        dp[j] = min(dp[j], new_d)

                        candidates_indices.add(j)

            que = deque([(i, dp[i]) for i in candidates_indices])

        return min([q[1] for q in que])
