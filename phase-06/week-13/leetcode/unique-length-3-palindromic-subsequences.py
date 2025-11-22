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



# BIT MANIPULATION SOLUTION
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # prefix sum + suffix sum + bit manipulation
        # instead of frequency arrays for each index, we use a bit mask to keep track
        # of the letters seen to the right and to the left of each letter

        prefix = []
        mask = 0
        for i in s:
            prefix.append(mask)
            letter = ord(i) - 96
            mask |= (1 << letter)
        
        suffix = []
        mask = 0

        for i in s[::-1]:
            suffix.append(mask)
            letter = ord(i) - 96
            mask |= (1 << letter)


        suffix.reverse()

        pals = set()
        for i in range(len(s)):
            curr = s[i]
            pre_mask = prefix[i]
            suff_mask = suffix[i]

            for j in range(27):
                if pre_mask & (1 << j) and suff_mask & (1 << j):
                    pal = chr(96 + j) + curr + chr(96 + j)
                    pals.add(pal)

        return len(pals)







class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        prefix = []
        curr = 0
        for i in s:
            prefix.append(curr)
            curr |= 1 << (ord(i) - ord('a'))

        suffix = []
        curr = 0
        for i in s[::-1]:
            suffix.append(curr)
            curr |= 1 << (ord(i) - ord('a'))

        suffix.reverse()

        per_letter = [0 for _ in range(26)]

        for i in range(1, len(s) - 1):
            pre = prefix[i]
            suf = suffix[i]
            for j in range(26):
                if (pre & (1 << j)) and (suf & (1 << j)):
                    per_letter[ord(s[i]) - ord('a')] |= 1 << j

        return sum(letter.bit_count() for letter in per_letter)

        



        



        
