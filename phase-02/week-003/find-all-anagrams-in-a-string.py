class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        k1, k2 = len(p), len(s) # respective lengths
        cp, cs = Counter(p), Counter(s[:k1]) # the sliding window

        if cp == cs: # first iteration, if the first window is an anagram
            res.append(0)

        for i in range(1, k2 - k1 + 1):
            last, new = s[i-1], s[i + k1 -1]

            cs[last] -= 1
            if cs[last] == 0:
                cs.pop(last)
            if new in cs:
                cs[new] += 1
            else:
                cs[new] = 1

            if cs == cp:
                res.append(i)

        return res