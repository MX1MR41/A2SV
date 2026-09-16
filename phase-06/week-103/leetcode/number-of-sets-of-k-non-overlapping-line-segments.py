class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        # dp + prefix sum
        # let dp[i][j] = the number of ways to form j lines using i segments
        # the base case is dp[0][0] = 1 since with 0 points we can form 0 lines
        # the recurrence relation is dp[i][j] = dp[i - 1][j] + sum(dp[0...i - 1][j])
        # meaning j lines can be formed with i points as:
        # - just as they were at i - 1
        # - adding one line to the number of ways we formed j - 1 lines across points 0 to i - 1
        MOD = 10**9 + 7
        dp = [[0 for _ in range(k + 1)] for _ in range(n)]
        dp[0][0]  = 1
        pre = [d[:] for d in dp]

        for i in range(1, n):
            
            for j in range(k + 1):
                dp[i][j] = (dp[i][j] + dp[i - 1][j]) % MOD
                if j > 0:
                    dp[i][j] = (dp[i][j] + pre[i - 1][j - 1]) % MOD

            for j in range(k + 1):
                pre[i][j] = (pre[i][j] + pre[i - 1][j] + dp[i][j]) % MOD
            


        return dp[-1][k]
                
