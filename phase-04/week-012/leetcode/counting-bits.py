class Solution:
    def countBits(self, n: int) -> List[int]:
        # bit manipulation + dp
        # if we & a number with number - 1, we remove the least significant bit
        # and get a lower number WHICH we could have already calculated
        dp = [0] * (n+1)

        for i in range(1, n+1):
            one_bit_offset = i & (i - 1)
            dp[i] = dp[one_bit_offset] + 1

        return dp
        
