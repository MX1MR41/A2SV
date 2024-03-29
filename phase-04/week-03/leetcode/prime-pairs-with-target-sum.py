class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        # use the sieve of eratosthenes method to find all primes within range
        primes = [True for _ in range(n+1)]
        primes[0] = primes[1] = False
        i = 2
        while i < n:
            if primes[i]:
                j = i * 2
                while j <= n:
                    primes[j] = False

                    j += i
            i += 1

        res = []
        # then use a two pointer approach to find valid combinations
        l, r = 0, n
        while l <= r:
            # find the leftmost next prime
            while l <= r and not primes[l]: l += 1
            # find the rightmost next prime
            while r >= l and not primes[r]: r -= 1

            if l + r == n: 
                res.append([l,r])
                l += 1
                r -= 1
            elif l + r < n: l += 1
            else: r -= 1

        return res
