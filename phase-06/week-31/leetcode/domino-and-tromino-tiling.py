class Solution:
    def numTilings(self, n: int) -> int:
        # dp + prefix sum
        # to fill the board upto n, we could either add 1 vertical domino from n-1;
        # or add two horizonatl dominoes to n - 2; or for every n <= n -3, we could find a way
        # to fit a combination of two trominoes with multiple dominoes, and we could mirror that
        # unique combination so there would be two ways.
        # So to fill a board of size n, we can take dp[n - 1] or dp[n - 2] or 2 * (sum(dp[0...n-3]))
        # we could store the sum in a prefix sum for ease
        MOD = 10**9 + 7

        if n <= 2:
            return n

        dp = [0] * (n + 1)

        
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2

        prefixdp = dp[:]
        prefixdp[1] = 2
        prefixdp[2] = 4

        
        for k in range(3, n + 1):
            dp[k] = (dp[k - 1] + dp[k - 2] + 2 * prefixdp[k - 3]) % MOD

            prefixdp[k] = (prefixdp[k - 1] + dp[k]) % MOD

        return dp[n]
