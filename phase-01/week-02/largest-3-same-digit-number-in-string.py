class Solution:
    def largestGoodInteger(self, num: str) -> str:
        l, r = 0, 2
        ans = ""
        while r < len(num):
            p = Counter(num[l:r+1])
            if len(p) == 1:
                good = num[l:r+1]
                if ans:
                    ans = max(ans, good)
                else:
                    ans = good
                r += 1
                l += 1
            else:
                r += 1
                l += 1

        return ans

