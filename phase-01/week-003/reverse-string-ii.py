class Solution:
    def reverseStr(self, s: str, k: int) -> str:

        ans = ""

        parts = [s[i:i+2*k] for i in range(0,len(s), 2*k)]

        for part in parts:
            if len(part) > k:
                ans += part[:k:][::-1] + part[k:]
            else:
                ans += part[::-1]

        return ans
        