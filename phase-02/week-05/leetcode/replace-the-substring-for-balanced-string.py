class Solution:
    def balancedString(self, s: str) -> int:
        cnt = Counter(s)
        l ,res = 0, len(s)

        for r in range(len(s)):
            cnt[s[r]] -= 1

            while l < len(s) and all( len(s)//4 >= cnt[j] for j in "QWER"):
                res = min(res, r - l + 1)
                cnt[s[l]] += 1
                l += 1

        return res

        
        
        