class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        # use dp to find the minimum value from the row above
        n = len(grid)
        dp = [[0] * n for _ in range(n)]

        for j in range(n):
            dp[0][j] = grid[0][j]

        for i in range(1, n):
            for j in range(n):
                dp[i][j] = min(dp[i-1][c] for c in range(n) if c != j) + grid[i][j]

        return min(dp[-1])
