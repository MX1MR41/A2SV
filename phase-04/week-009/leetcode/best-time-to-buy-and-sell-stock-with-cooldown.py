class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # modified code from 
        # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

        # added a third dimension which stores the cooldown profit
        # i.e. if we sold a stock the previous day, we cannot buy today
        # so the cooldown value for today is the same as the stock-less(sell) value of today-1
        # and among the ways we can be stock-less today is also the cooldown of yesterday
        n = len(prices)
        if n <= 1: return 0
        dp = [[0]*3 for _ in range(n)]

        dp[0][0] = 0
        dp[0][1] = -prices[0] 
        dp[0][2] = 0

        dp[1][0] = max(0, dp[0][1] + prices[1])
        dp[1][1] = max(dp[0][1], - prices[1]) 
        dp[1][2] = 0

        for day in range(1, n):
            
            dp[day][0] = max(dp[day-1][0], dp[day-1][1] + prices[day], dp[day-1][2])
            # the stock-less profit of yesterday
            # selling the stock-full of yesterday 
            # the stock-less cooldown of yesterday

            dp[day][1] = max(dp[day-1][1], dp[day-2][0] - prices[day])
            # the stock-full of yesteday
            # buying today's stock by the profit of before yesterday's stock-less, 
            # cuz we can't buy today if we sold tomorrow

            dp[day][2] = dp[day-1][0]
            # the cooldown profit of today is the stock-less profit of yesterday
            # i.e. not buying a stock today after selling(becoming stock-less) yesterday


        return dp[-1][0]


# shorter version

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stock = (-prices[0], 0)
        stockless = (0, 0)
        prevstockless = (0, -1)

        ans = 0

        for i in range(1, len(prices)):
            sell = stock[0] + prices[i]

            currstockless = stockless
            if sell > stockless[0]:
                currstockless = (sell, i)

            buy = prevstockless[0] - prices[i]
            if buy > stock[0]:
                stock = (buy, i)

            if stockless[0] > prevstockless[0]:
                prevstockless = stockless

            stockless = currstockless

            ans = max(stock[0], stockless[0], prevstockless[0])

        return ans

