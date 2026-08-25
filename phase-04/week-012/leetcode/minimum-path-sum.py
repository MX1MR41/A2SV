class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [[0] * n for _ in range(m)]

        dp[-1][-1] = grid[-1][-1]

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if i == m-1 and j == n-1:
                    continue
                elif j == n-1:
                    down, right = dp[i+1][j], float("inf")
                elif i == m-1:
                    down, right = float("inf"), dp[i][j+1]
                else:
                    down, right = dp[i+1][j], dp[i][j+1]

                dp[i][j] = grid[i][j] + min(down, right)

        return dp[0][0]

