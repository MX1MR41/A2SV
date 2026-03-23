class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7

        dp = [[[0, 0] for _ in range(n)] for _ in range(m)]

        dp[0][0] = [grid[0][0], grid[0][0]]

        for j in range(1, n):
            dp[0][j][0] = dp[0][j - 1][0] * grid[0][j]
            dp[0][j][1] = dp[0][j - 1][1] * grid[0][j]

        for i in range(1, m):
            dp[i][0][0] = dp[i - 1][0][0] * grid[i][0]
            dp[i][0][1] = dp[i - 1][0][1] * grid[i][0]

        for i in range(1, m):
            for j in range(1, n):
                cell = grid[i][j]

                candidates = (
                    dp[i - 1][j][0] * cell,
                    dp[i - 1][j][1] * cell,
                    dp[i][j - 1][0] * cell,
                    dp[i][j - 1][1] * cell,
                )

                dp[i][j][0] = min(candidates)
                dp[i][j][1] = max(candidates)

        max_prod = dp[-1][-1][1]

        return max_prod % MOD if max_prod >= 0 else -1
