class Solution:
    def __init__(self):

        self.sieve = [True] * (10**6 + 1)
        self.sieve[0] = self.sieve[1] = False
        for i in range(2, 10**6 + 1):
            if self.sieve[i]:
                for j in range(i * i, 10**6 + 1, i):
                    self.sieve[j] = False

    def closestPrimes(self, left: int, right: int) -> List[int]:
        res = [float("-inf"), float("inf")]

        i = left
        while i <= 10**6 and not self.sieve[i]:
            i += 1

        j = i + 1
        while j <= 10**6 and j <= right:
            while j <= 10**6 and j <= right and not self.sieve[j]:
                j += 1

            if j <= 10**6 and j <= right and self.sieve[j] and self.sieve[i]:

                if j - i < res[1] - res[0]:
                    res = [i, j]

                i = j
                j += 1

        return res if res != [float("-inf"), float("inf")] else [-1, -1]
