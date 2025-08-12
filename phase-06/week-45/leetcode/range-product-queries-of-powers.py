class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # prefix product
        # any number can be represented as powers of two
        # the powers can be computed from the binary representation of the number
        # wherever a bit i is set, then 2^(i) is a power that makes up n
        powers = []
        for i in range(32):
            if n & (1 << i):
                powers.append(2**i)

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
