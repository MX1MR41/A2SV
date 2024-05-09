class Solution:
    def tribonacci(self, n: int) -> int:
        dp = {0: 0, 1: 1, 2: 1}
        def tri(x):

            if x in dp:
                return dp[x]

            dp[x] = tri(x-1) + tri(x-2) + tri(x-3)
            return dp[x]

        return tri(n)
        
