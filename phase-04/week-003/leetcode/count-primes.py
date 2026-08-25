class Solution:
    def countPrimes(self, n: int) -> int:
        if not n: return 0
        ps = [True for _ in range(n+1)]
        ps[0] = ps[1] = False

        i = 2

        while i <= n:
            if ps[i]:
                j = i * 2

                while j <= n:
                    ps[j] = False
                    j += i

            i += 1


        return ps[:n].count(True)
        