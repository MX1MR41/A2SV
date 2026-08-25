class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        # dp
        # start from the leftmost column; for each cell check if a valid move is possible

        m, n = len(grid), len(grid[0])
        dirs = [(-1, 1), (0, 1), (1, 1)]
        valid = lambda i, j: 0 <= i < m and 0 <= j < n

        dp = [[0] * n for _ in range(m)]

        ans = 0

        for j in range(n - 1):
            for i in range(m):

                curr = dp[i][j]
                # if curr != j it means that this cell wasn't and can't be visited from the left
                if curr != j:
                    continue

                for d_i, d_j in dirs:
                    new_i, new_j = i + d_i, j + d_j

                    if valid(new_i, new_j) and grid[new_i][new_j] > grid[i][j]:
                        dp[new_i][new_j] = max(dp[new_i][new_j], curr + 1)
                        ans = max(ans, dp[new_i][new_j])

        return ans
