class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7

        if n == 0:
            return 1 
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp = [0] * (n + 1)

        # Base cases
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2

        # Calculate dp[k] using the O(k) sum
        for k in range(3, n + 1):
            # Contribution from ending with V (m=1)
            dp[k] = dp[k - 1]
            # Contribution from ending with HH (m=2)
            dp[k] = (dp[k] + dp[k - 2]) % MOD

            # Contribution from ending with irreducible blocks of size m >= 3
            # Summation: 2 * dp[k-3] + 2 * dp[k-4] + ... + 2 * dp[0]
            for j in range(k - 3, -1, -1): # Loop from j=k-3 down to 0
                dp[k] = (dp[k] + (2 * dp[j]) % MOD) % MOD

        return dp[n]
