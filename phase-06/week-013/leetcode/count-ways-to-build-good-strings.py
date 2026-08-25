class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # dp
        # for every valid string, we can form two more from it
        # either by adding ones or by adding zeros
        # performing the updates only for the next two string prevents future overcounting
        
        dp = [0]*(high + 1)
        dp[one] += 1
        dp[zero] += 1

        for i in range(high):
            if not dp[i]:
                continue

            nxt = i + one
            if nxt <= high:
                dp[nxt] += dp[i]

            nxt = i + zero
            if nxt <= high:
                dp[nxt] += dp[i]
            
    
        return sum(dp[low: high + 1]) % (10**9 + 7)


            
        
