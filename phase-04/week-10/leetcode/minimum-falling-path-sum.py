class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # modified code from https://leetcode.com/problems/minimum-falling-path-sum-ii/


        n = len(matrix)
        dp = [[0] * n for _ in range(n)]

        for j in range(n):
            dp[0][j] = matrix[0][j]

        for i in range(1, n):
            for j in range(n):
                if 1 <= j <= n-2:
                    dp[i][j] = min(dp[i-1][c] for c in range(j-1, j+2)) + matrix[i][j]
                elif j == 0:
                    dp[i][j] = min(dp[i-1][c] for c in range(2)) + matrix[i][j]
                else:
                    dp[i][j] = min(dp[i-1][c] for c in range(n-2, n)) + matrix[i][j]

        return min(dp[-1])

        
