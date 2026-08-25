class Solution:
    # modified code from https://leetcode.com/problems/longest-common-subsequence/
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0

        m, n = len(text1), len(text2)
        dp = [[0]*n for _ in range(m)]


        for i in range(m - 1, -1, -1):
            a = text1[i]
            for j in range(n- 1, -1, -1):
                b = text2[j]
                if a == b:
                    dp[i][j] = dp[i + 1][j + 1] + 1 if i + 1 < m and j + 1 < n else 1
      
                else:
                    down = dp[i + 1][j] if i + 1 < m else 0
                    right = dp[i][j + 1] if j + 1 < n else 0
                    dp[i][j] = max(down, right)

        return dp


    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # dp + two pointers
        # we build the result string by iterating over the strings in parallel using two pointers
        # and choosing to add a letter X over letter Y if the LCS of the string after X 
        # and the string including and after Y is greater than the other way around.
        # formally, X = s1[i], Y = s2[j], if LCS(s1[i+1:], s2[j:]) >= LCS(s1[i:], s2[j+1:]) 
        # we choose X because the more letters in common the remaining strings have, the less letters
        # we would need to build our supersequence string, hence the shorter the supersequence becomes

        res = ""
        i = 0
        j = 0

        # get a dp matrix LCS, where LCS[i][j] represents the length of the longest common sub
        # for the strings s1[i:] and s2[j:]
        LCS = self.longestCommonSubsequence(str1, str2)

        # two pointers
        while i < len(str1) and j < len(str2):
            a = str1[i]
            b = str2[j]

            # in this case, we can just add one occurence of said letter since it occurs in both
            if a == b:
                res += a
                i += 1
                j += 1
                continue

            # the length of the LCS of s1 after a
            LCSa = LCS[i + 1][j] if i + 1 < len(LCS) else 0

            # the length of the LCS f s2 after b
            LCSb = LCS[i][j + 1] if j + 1 < len(LCS[0]) else 0

            # choose based on the LCS's
            if LCSa >= LCSb:
                res += a
                i += 1
            else:
                res += b
                j += 1

        # take care of any remaining letters in either s1 or s2
        while i < len(str1):
            res += str1[i]
            i += 1

        while j < len(str2):
            res += str2[j]
            j += 1

        return res

        
