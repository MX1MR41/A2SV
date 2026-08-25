class Solution:
    def numSquares(self, n: int) -> int:
        # unbounded knapsack dp
        i = 1
        s = []
        dp = [float("inf")] * (n+1)

        while i ** 2 <= n:
            s.append(i**2)
            dp[i**2] = 1
            i += 1


        for i in range(2, n+1):
            for j in s:
                left = i - j
                if left < 0: break

                dp[i] = min(dp[i], dp[left] + dp[j])

        return dp[-1]

        
