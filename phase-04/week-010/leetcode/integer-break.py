class Solution:
    def integerBreak(self, n: int) -> int:
        # bottom-up dp
        # for a number x = a + b where both a and b are > 0, the answer for x will be
        # a multiplication of max(a, dp[a]) and max(b, dp[b])
        dp = [0] * (n+1)

        dp[0] = 0
        dp[1] = 0
        dp[2] = 1

        for curr in range(2, n+1):
            for sub in range(2, curr):
                left = curr - sub
                if left > 0:
                    dp[curr] = max(dp[curr], (max(left, dp[left])*max(sub, dp[sub])))

        return dp[n]

        
