class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        d = Counter()
        res = 0
        l = 0
        for r in range(len(s)):
            rlet = s[r]
            d[rlet] += 1
            while d[rlet] > 2:s
                llet = s[l]
                d[llet] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res

        
