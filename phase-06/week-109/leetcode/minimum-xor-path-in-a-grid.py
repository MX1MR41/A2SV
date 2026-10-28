class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[-1][-1].add(grid[-1][-1])
        for i in range(m - 2, -1, -1):
            for v in dp[i + 1][-1]:
                dp[i][-1].add(v ^ grid[i][-1])

        for j in range(n -2, -1, -1):
            for v in dp[-1][j + 1]:
                dp[-1][j].add(v ^ grid[-1][j])


        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                for v in dp[i + 1][j]:
                    dp[i][j].add(v ^ grid[i][j])

                for v in dp[i][j + 1]:
                    dp[i][j].add(v ^ grid[i][j])

        return min(dp[0][0])
