class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        if n == 0: return 0

        # indices: 0 = Flat, 1 = Long (Holding), 2 = Short (Owed)
        # Initialize with -infinity because temporary profit can be negative
        dp = [[float('-inf')] * 3 for _ in range(k + 1)]
        
        # Base Case: 0 transactions completed, we have 0 profit.
        dp[0][0] = 0 
        
        for price in prices:
            # Create a copy for the current day
            new_dp = [row[:] for row in dp]

            for j in range(1, k + 1):
                # 1. Calculate LONG state for transaction j
                # Either keep holding, or buy (transition from Flat of PREVIOUS transaction j-1)
                new_dp[j][1] = max(dp[j][1], dp[j-1][0] - price)

                # 2. Calculate SHORT state for transaction j
                # Either keep holding short, or sell short (transition from Flat of PREVIOUS transaction j-1)
                new_dp[j][2] = max(dp[j][2], dp[j-1][0] + price)

                # 3. Calculate FLAT state for transaction j
                # Either stay flat, or Close Long (+price), or Close Short (-price)
                # We use dp[j] (yesterday's holdings) to ensure we hold for at least 1 day
                new_dp[j][0] = max(dp[j][0], dp[j][1] + price, dp[j][2] - price)

            # CRITICAL: Update dp table AFTER processing all transactions for the day
            dp = new_dp

        # Result is the max profit of any transaction count ending in a Flat state
        return max(row[0] for row in dp)
