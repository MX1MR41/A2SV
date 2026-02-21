class Solution:
    def __init__(self):
        self.sieve = [True] * (30)
        self.sieve[0] = self.sieve[1] = False
        for i in range(2, 30):
            m = 2
            while i * m < 30:
                self.sieve[i * m] = False
                m += 1
            

    def countPrimeSetBits(self, left: int, right: int) -> int:
        res = 0
        for num in range(left, right + 1):
            bits = num.bit_count()
            if self.sieve[bits]:
                res += 1

        return res
        
