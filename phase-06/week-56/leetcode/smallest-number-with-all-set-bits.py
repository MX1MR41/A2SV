class Solution:
    def smallestNumber(self, n: int) -> int:
        if n.bit_length() == n.bit_count():
            return n 
            
        return (1 << n.bit_length()) - 1
