class Solution:
    def countCommas(self, n: int) -> int:
        res = 0
        curr = 1000

        while curr <= n:
            res += n - curr + 1
            curr *= 1000

        return res
        

