class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        
        x = ceil(log(n,3))

        if 3 ** x != n:
            return False

        res = self.isPowerOfThree(n//3**x)

        return res
        