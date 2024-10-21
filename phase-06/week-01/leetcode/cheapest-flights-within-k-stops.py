class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        # sssp algorithm

        dp = [float("inf")] * n
        dp[src] = 0

        for _ in range(k + 1):

            temp_dp = dp[:]

            for u, v, p in flights:
                if dp[u] != float("inf"):  # only if u has been reached before in a previous iteration
                    temp_dp[v] = min(temp_dp[v], dp[u] + p)

            dp = temp_dp

        return dp[dst] if dp[dst] != float("inf") else -1
