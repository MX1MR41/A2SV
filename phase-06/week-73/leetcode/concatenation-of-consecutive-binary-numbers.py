class Solution:
    def concatenatedBinary(self, n: int) -> int:
        # bit
        # just left shift (multiply by 2) the previous number by x 
        # where x is the bit_length of the the number to be concatenated, then add that number
        res = 0
        MOD = 1000000007
        for i in range(1, n + 1):
            res = (res * (2 **(i.bit_length())) + i) % MOD

        return res
        
