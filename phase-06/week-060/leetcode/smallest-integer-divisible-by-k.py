class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
   
        remainder = 0
        

        # We iterate through lengths 1, 2, 3...
        # We keep updating the remainder of the number "1", "11", "111", etc.
        for length in range(1, k + 1):
            # Formula: next_remainder = (prev_remainder * 10 + 1) % k
            remainder = (remainder * 10 + 1) % k
            
            # If remainder is 0, we found a number divisible by k
            if remainder == 0:
                return length
                
        return -1
