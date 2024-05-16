class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2: return 0
        
        dp = [[0]*2 for _ in range(n)]
        
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], -prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
        
        dp2 = [[0]*2 for _ in range(n)]
        
        dp2[0][0] = -prices[0]
        dp2[0][1] = 0
        
        for i in range(1, n):
            dp2[i][0] = max(dp2[i-1][0], dp[i-1][1] - prices[i])
            dp2[i][1] = max(dp2[i-1][1], dp2[i-1][0] + prices[i])
        
        return dp2[-1][1]
