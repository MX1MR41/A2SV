class Solution:
    def romanToInt(self, s: str) -> int:
        numap = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D": 500, "M": 1000}
        dec = 0
        for i in range(len(s)):
            if i > 0 and numap[s[i]] > numap[s[i - 1]]:
                dec += numap[s[i]] - 2 * numap[s[i - 1]]
            else:
                dec += numap[s[i]]
        return dec
