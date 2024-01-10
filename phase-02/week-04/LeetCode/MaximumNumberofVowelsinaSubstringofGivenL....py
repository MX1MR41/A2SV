class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l, n = 1, len(s)
        vow = {'a','e', 'i', 'o', 'u'}
        curr = 0
        for i in range(k):
            if s[i] in vow:
                curr += 1

        res = curr
        
        for i in range(1, n - k +1):
            prev, next = s[i-1], s[i + k - 1]

            if prev in vow:
                curr -= 1
            if next in vow:
                curr += 1
            res = max(res, curr)

        return res