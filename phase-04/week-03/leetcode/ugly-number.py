class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False
        # if 2,3 and 5 are the only primes, then prime-factorizing 
        # the number with only these three would lead to 1
        
        while n != 1 :
            if not n % 2:
                n //= 2
            elif not n % 3:
                n //= 3
            elif not n % 5:
                n //= 5
            else:
                return False

        return True
        