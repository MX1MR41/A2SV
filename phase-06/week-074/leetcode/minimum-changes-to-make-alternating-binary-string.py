class Solution:
    def minOperations(self, s: str) -> int:
        return min (
            (sum(1 for i in range(0, len(s), 2) if s[i] == "1") 
            + sum(1 for i in range(1, len(s), 2) if s[i] == "0")), 
            
            (sum(1 for i in range(0, len(s), 2) if s[i] == "0") 
            + sum(1 for i in range(1, len(s), 2) if s[i] == "1"))
            )
        
