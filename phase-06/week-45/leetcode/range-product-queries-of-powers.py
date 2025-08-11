class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # prefix product
        powers = []
        need_one = True
        while n > 0 and log2(n) > 0:
            p = int(log2(n))
            if log2(n) == p:
                need_one = False

            powers.append(2**p)

            n -= 2**p

        if need_one:
            powers.append(1)

        powers.reverse()

        for i in range(1, len(powers)):
            powers[i] *= powers[i - 1]

        res = []
        mod = 10**9 + 7
        for s, e in queries:
            prod = powers[e]
            if s > 0:
                prod //= powers[s - 1]

            res.append(int(prod % mod))

        return res
