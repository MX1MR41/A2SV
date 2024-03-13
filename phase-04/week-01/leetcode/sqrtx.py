class Solution:
    def mySqrt(self, x: int) -> int:
        if not x: return x
        l, r = 1 , x

        res = l

        while l <= r:
            mid = (l+r)//2

            if mid * mid  <= x:
                l = mid + 1
                res = mid
            else:
                r = mid - 1

        return res
        