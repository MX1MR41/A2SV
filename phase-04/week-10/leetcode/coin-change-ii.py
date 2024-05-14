class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        # to avoid double counting the same combinations, we iterate over each amount
        # for each coin instead of each coin for each amount. Once we have checked a coin
        # for a certain amount, there is no need for us to check for that amount again.
        for coin in coins:
            for curr in range(coin, amount + 1):

                left = curr - coin
                dp[curr] += dp[left]

 
        return dp[-1]
        
