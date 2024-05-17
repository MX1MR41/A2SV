class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # use two dp arrays dp and dp2 where dp[i][0] stores the maximum profit you can have on the
        # i'th day if you have some stock at the end of the day and you haven't done any transaction
        # dp[i][1] stores maxi profit you can have on i'th day if you have made only one transaction
        # and you have no stock in hold at the end of the day
        # dp2[i][0] stores the maximum profit you can have at the end of i'th day if you still have
        # some stock in hold 
        # dp2[i][1] store the maximum profit you can have at the end of i'th day if you have performed
        # at most two transactions and you have no stock in hold at the end of the day
        n = len(prices)
        if n < 2: return 0
        
        dp = [[0]*2 for _ in range(n)]
        
        dp[0][0] = -prices[0] # only way to have stock on this day is to buy the first stock
        dp[0][1] = 0
        
        # dp[i][1] will maximize the profit of performing ONE transaction
        for i in range(1, n):
            # either keep the stock you had yesterday OR buy today's stock
            dp[i][0] = max(dp[i-1][0], -prices[i])
            # either sell yesterday's stock at today's price OR stay as stockless as yesterday
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
        
        dp2 = [[0]*2 for _ in range(n)]
        
        dp2[0][0] = -prices[0]
        dp2[0][1] = 0
        
        # dp2[i][1] will maximize the profit of performing TWO transactions by getting the maximized
        # profit of ONE transaction from dp and processing with that info
        for i in range(1, n):
            # either hold the stock from yesterday OR buy today's stock
            dp2[i][0] = max(dp2[i-1][0], dp[i-1][1] - prices[i])
            # either stay as stockless as yesterday OR sell yesterdays stock at today's price
            dp2[i][1] = max(dp2[i-1][1], dp2[i-1][0] + prices[i])
        
        return dp2[-1][1]
