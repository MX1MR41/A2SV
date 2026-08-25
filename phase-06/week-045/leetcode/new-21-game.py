class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # sliding window + dp

        if k == 0:
            return 1.0
        if n >= k - 1 + maxPts:
            return 1.0

        size = k + maxPts
        dp = [0.0] * (size)

        for x in range(k, size):
            dp[x] = 1.0 if x <= n else 0.0

        window_sum = sum(dp[k : k + maxPts])

        for x in range(k - 1, -1, -1):
            dp[x] = window_sum / maxPts

            window_sum += dp[x] - dp[x + maxPts]

        return dp[0]
