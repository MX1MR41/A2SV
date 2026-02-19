class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # prefix sum  + sliding window
        
        pre = []
        z = 0
        n = len(s)
        for i in range(n):
            pre.append(z)
            if s[i] == "0":
                z += 1
            else:
                z = 0

        suf = []
        z = 0
        for i in range(n - 1, -1, -1):
            suf.append(z)
            if s[i] == "0":
                z += 1
            else:
                z = 0

        suf.reverse()

        res = 0
        l = 0
        for r in range(n):
            if s[r] == "0":
                l = r + 1
                continue

            left = pre[l]
            right = suf[r]

            if left >= r - l + 1:
                res += 1

            res += min(right, r - l + 1)

            left = min(r - l, left)
            right = min(r - l, right)

            if left > 0 and right > 0 and left + right >= r - l + 1:
                sub_len = 2 * (r - l + 1)

                res += sub_len - 2 * (r - l + 1)

        return res
