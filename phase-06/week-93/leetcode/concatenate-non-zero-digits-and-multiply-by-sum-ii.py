class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        # prefix sum + math
        # use modular inverse arithmetic 
        MOD = 10**9 + 7
        n = len(s)

        # 1. Precompute powers of 10 and their Modular Inverses
        # We need this to replace the slow (10 ** p) and the division (//)
        pow10 = [1] * (n + 1)
        inv10 = [1] * (n + 1)

        # The modular inverse of 10 modulo 10^9+7
        INV_10 = pow(10, MOD - 2, MOD)

        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD
            inv10[i] = (inv10[i - 1] * INV_10) % MOD

        suff = []
        psuff = []

        current_val = 0
        p = 0

        for char in s[::-1]:
            if char != "0":
                digit = int(char)

                current_val = (current_val + digit * pow10[p]) % MOD
                p += 1

            suff.append(current_val)
            psuff.append(p)

        suff.reverse()
        psuff.reverse()

        pre = []
        current_sum = 0
        for char in s:
            current_sum += int(char)
            pre.append(current_sum)

        res = []
        for l, r in queries:

            num = suff[l] - suff[r + 1] if r + 1 < n else suff[l]
            num %= MOD

            extra = psuff[r + 1] if r + 1 < n else 0

            num = (num * inv10[extra]) % MOD

            summ = pre[r] - pre[l - 1] if l - 1 >= 0 else pre[r]
            summ %= MOD

            curr = (summ * num) % MOD
            res.append(curr)

        return res
