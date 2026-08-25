class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        gcd = math.gcd(2,n)
        return int(2*n/gcd)