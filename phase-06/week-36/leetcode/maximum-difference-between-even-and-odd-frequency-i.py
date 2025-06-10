class Solution:
    def maxDifference(self, s: str) -> int:
        cnt = Counter(s)
        odd = 0
        even = float("inf")
        for i, j in cnt.items():
            if j % 2:
                odd = max(odd, j)
            else:
                even = min(even, j)

        return odd - even 

        
