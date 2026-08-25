class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp: at each index i, dp[i] hold the largest stock price in days after i
        n = len(prices)
        dp = [0] * n
        dp[-1] = prices[-1]
        res = 0
        for i in reversed(range(n-1)):
            dp[i] = max(prices[i], dp[i+1])
            stock = prices[i]
            res = max(res, dp[i] - stock) 


        return res

            
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # better approach: at each index i, m will store the minimum seen so far before i
        # M will assume i is the maximum and just compute as such
        prof = 0
        n = len(prices)
        m = prices[0]
        for i in range(1,n):
            M = prices[i]
            if M < m:
                m = M
            else:
                diff = M - m
                prof = max(prof, diff)

        return prof
        
