class Solution:
    def longestPalindrome(self, s: str) -> str:
        # two pointers
        # brute force way would be to check every substring by combining every possible l and r
        # optimized: instead of checking palindrome-icity of substrings from ends, 
        # check from the middle. For every index i, assume it to be the middle of the palindrome
        # then use two pointers that move outwards to check how long of a valid palindrome
        # is present as a substring in the string
        
        res = ""
        n = len(s)
        for i in range(n):
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l:r + 1]
                l -= 1
                r += 1

        for i in range(n):
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l:r + 1]
                l -= 1
                r += 1

        return res
        
