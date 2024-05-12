class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        # 2d array dp where dp[day] represents our maximum profit on that day
        # dp[day][0] => profit if we still have any stock on that day (either bought today or kept from past)
        # dp[day][1] => profit if we have not stock on that day (sold last one)
        dp = [[0]*2 for _ in range(n)]

        dp[0][0] = 0 # first day we got no stock ans we don't buy any, so 0 profit
        dp[0][1] = -prices[0] # if we buy the first day's stock then our profit is essentially -cost of stock

        for day in range(1, n):
            
            dp[day][0] = max(dp[day-1][0], dp[day-1][1] + prices[day] - fee)
            # two ways we can be stock-less on this day: 
            # 1) stay stockless ever since the last day we sold our last stock in which case our profit
            # remains the same as the profit from the day we were last stock-less.
            # 2) sell our last remaining stock on this day. The calculation works cuz -stock[prev_day]
            # was already stored in the profit of having a stock (i.e. dp[...][1])
            # choose the maximum profit from these two options


            dp[day][1] = max(dp[day-1][1], dp[day-1][0] - prices[day])
            # 1) we can keep the stock from the last day we had stock
            # 2) we can buy a stock today
            # choose the maximum profit from these two


        return dp[-1][0]
