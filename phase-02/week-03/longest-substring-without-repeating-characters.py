class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        res = 0
        n = len(s)
        if not n:
            return 0
        wind = {} # hashmap that maps elements to their indices

        while r < n:
            chr = s[r]

            if chr in wind:
                l = wind[chr] + 1
                r = l
                wind = {}
            else:
                wind[chr] = r
                r += 1
                res = max(res, r - l)


        return res