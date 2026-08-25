class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        def check(mid):
            res = wind = sum([abs(ord(i)-ord(j)) for i,j in zip(s[:mid],t)])

            for r in range(mid, n):
                wind += abs(ord(s[r]) - ord(t[r]))
                wind -= abs(ord(s[r-mid]) - ord(t[r-mid]))

                res = min(res,wind)
            return res <= maxCost

        ans = 0
        l, r = 1, n
        while l <= r:
            mid = (l+r)//2
            if check(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return ans
            

        
        