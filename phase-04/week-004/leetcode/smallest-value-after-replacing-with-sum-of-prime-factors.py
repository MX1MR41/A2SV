class Solution:
    def smallestValue(self, n: int) -> int:
        def primes(x):
            tot = 0
            i = 2
            while x > 1:
                while not x % i:
                    tot += i
                    x //= i

                i += 1
            return tot

        while True:
            ans = primes(n)
            if ans == n: return n

            n = ans
