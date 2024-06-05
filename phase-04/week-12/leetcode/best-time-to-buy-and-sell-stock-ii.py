class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # bottom-up dp where dp is a len(prices) X 2 array
        # dp[i][0] = max profit possible on i-th day while having no stock in hand
        # dp[i][1] = max profit possible on i-th day while still having some stock in hand
        n = len(prices)

        dp = [[0]*2 for _ in range(n)]
        # only way we could have stock on the 0th day is by buying that day's stock 
        # and profit will be -prices[0], cost of that day's stock
        dp[0] = [0, -prices[0]]

        for i in range(1, n):

            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            # two ways to become stockless on the i-th day
            # 1) stay as stockless as you were yesterday
            # 2) sell the last stock you had in hand yesterday i.e. (i-1)-th day

            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i], dp[i][0] - prices[i])
            # three ways to become stock-full on the i-th day
            # 1) keep the same stock you had yesterday
            # 2) buy today's stock from when you were stock-less YESTERDAY
            # 3) buy today's stock from when you were stock-les TODAY

        return dp[-1][0]
