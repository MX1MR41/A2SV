class Solution:
    def minFlips(self, s: str) -> int:
        # sliding window
        n = len(s)
        s += s

        o_odd = o_even = z_odd = z_even = 0

        res = float("inf")

        l = 0
        for r in range(2 * n):
            if r % 2:
                if s[r] == "0":
                    z_odd += 1
                else:
                    o_odd += 1
            else:
                if s[r] == "0":
                    z_even += 1
                else:
                    o_even += 1

            if r - l + 1 < n:
                continue

            curr = min(z_odd + o_even, z_even + o_odd)
            res = min(res, curr)

            if l % 2:
                if s[l] == "0":
                    z_odd -= 1
                else:
                    o_odd -= 1
            else:
                if s[l] == "0":
                    z_even -= 1
                else:
                    o_even -= 1

            l += 1

        return res
