class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low + 1)//2 if (high - low + 1) % 2 == 0 else ((high - low + 1)//2 + 1 if low % 2 != 0 else (high - low + 1)//2)
        
