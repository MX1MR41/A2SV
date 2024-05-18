class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if m == 0: return True
        if n < m: return False
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if (i,j) == (0,0):
                    left = up = 0
                    diag = 0

                elif i == 0:
                    left, up = dp[i][j-1], 0
                    diag = 0
                elif j == 0:
                    up, left = dp[i-1][j], 0
                    diag = 0
                else:
                    up, left, diag = dp[i-1][j], dp[i][j-1], dp[i-1][j-1]

                
                if s[i] == t[j]:
                    dp[i][j] = 1 + diag
                else:
                    dp[i][j] = max(left, up)

        return dp[-1][-1] == m
