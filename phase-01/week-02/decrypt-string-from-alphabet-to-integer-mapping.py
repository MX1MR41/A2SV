class Solution:
    def freqAlphabets(self, s: str) -> str:
        alpha = 'abcdefghijklmnopqrstuvwxyz'

        HASH = {(str(i+1) if i < 9 else str(i+1) + '#'): x for i, x in enumerate(alpha)}

        ans = ''
        i, j = 0, len(s)

        while i < j:

            if i <= j - 3 and s[i+2] == '#':
                ans += HASH[s[i:i+3]] 
                i += 3 

            else:
                ans += HASH[s[i]]
                i += 1  

        return ans

        