class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        res = [float("inf"), ""]
        l = 0
        n = len(s)
        ones = 0
        for r in range(n):
            rnum = s[r]
            if rnum == "1":
                ones += 1

            while ones >= k:
                len_s = r - l + 1
                if len_s == res[0]:
                    if s[l:r + 1] < res[1]:
                        res[1] = s[l:r + 1]
                if len_s < res[0]:
                    res = [len_s, s[l:r + 1]]

                lnum = s[l]
                if lnum == "1":
                    ones -= 1

                l += 1

        return res[1]

            

        
