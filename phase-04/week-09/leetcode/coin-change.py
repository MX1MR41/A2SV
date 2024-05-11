class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # bottom-up dp
        
        dp = [float("inf")] * (amount+1)
        dp[0] = 0

        for i in range(1, amount+1): # precompute and compute previous and current values
            for coin in coins: # we see if taking this coin would be the optimal choice
                left = i - coin 
                if left >= 0: # if the remaining is negative; then no solution 
                    
                    # the optimal answer for i would be the minimum among
                    # all possible PICK-OR-DON'T-PICK coins
                    dp[i] = min(dp[i], 1 + dp[left])

        return dp[amount] if dp[amount] != float("inf") else -1
        
