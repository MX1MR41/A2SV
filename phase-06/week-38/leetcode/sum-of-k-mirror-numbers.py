class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def is_k_pal(p):

            s = []
            x = p
            while x:
                s.append(str(x % k))
                x //= k
            s = "".join(reversed(s))
            return s == s[::-1]

        res = []
        L = 1

        while len(res) < n:
            half_len = (L + 1) // 2
            start = 1 if half_len == 1 else 10 ** (half_len - 1)
            end = 10**half_len

            for h in range(start, end):
                s = str(h)

                if L % 2 == 0:
                    p = int(s + s[::-1])
                else:
                    p = int(s + s[-2::-1])

                if is_k_pal(p):
                    res.append(p)
                    if len(res) == n:
                        break

            L += 1

        return sum(res)
