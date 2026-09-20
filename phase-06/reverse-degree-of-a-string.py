class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum((i + 1) * (26 - (ord(s[i]) - ord('a'))) for i in range(len(s)))
        
