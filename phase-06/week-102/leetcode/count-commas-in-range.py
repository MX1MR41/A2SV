class Solution:
    def countCommas(self, n: int) -> int:
        return  max(n - 1000 + 1, 0)
        
