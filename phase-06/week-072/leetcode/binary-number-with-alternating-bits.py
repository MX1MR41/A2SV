class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # trust
        return all((min(1, n & (1<<i)) != min(1, n & (1 << (i - 1)))) for i in range(1, n.bit_length()))
        
