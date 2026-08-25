class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1

        res = (x if n % 2 else 1) * self.myPow(x * x, abs(n) // 2)
        
        return res if n >= 0 else 1/res