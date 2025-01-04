class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # prefix sum + suffix sum
        # prefix[i] will store a frequency array of the 26 letters seen just before i
        # suffix[i] will store a frequency array of the 26 letters seen just after i
        # for every letter in s, we check to in its suffix and prefix tables to see
        # if there is a common character on both of its sides; in which case it is a palindrome
        prefix = []
        pre = [0] * 26
        for i in s:
            prefix.append(pre[:])
            letter = ord(i) - 97
            pre[letter] += 1
        
        suffix = []
        suff = [0] * 26

        for i in s[::-1]:
            suffix.append(suff[:])
            letter = ord(i) - 97
            suff[letter] += 1

        suffix.reverse()

        pals = set()
        for i in range(len(s)):
            curr = s[i]
            for j in range(26):
                if prefix[i][j] and suffix[i][j]:
                    pal = chr(j + 97) + curr + chr(j + 97)
                    pals.add(pal)

        return len(pals)



        
