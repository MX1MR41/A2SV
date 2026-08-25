class Solution:
    def binaryGap(self, n: int) -> int:
        res = float("-inf")
        last = n.bit_length()
        for i in range(n.bit_length()):
            if n & (1 << i):
                res = max(res, i - last)
                last = i

        return max(res, 0)
        
