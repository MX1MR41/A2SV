class Solution:
    def climbStairs(self, n: int) -> int:
        # for each stair n, we could've reached it from either 
        # the (n-1)th or (n-2)th stair. So we could reach nth stair in total of
        # the (n-1)th's plus (n-2)th's possible permutations.
        # for the 0th and 1st stair tho, we reach either in only one way.
        if n <= 1:
            return 1

        dp = [0] * (n + 1)
    
        dp[0] = dp[1] = 1


        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
