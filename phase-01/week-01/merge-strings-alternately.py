class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans, extra = "", ""
        diff = abs(len(word1) - len(word2))

        if len(word1) > len(word2):
            extra += word1[-diff:]
            word1 = word1[:-diff]

        if len(word2) > len(word1):
            extra += word2[-diff:]
            word2 = word2[:-diff]

        for i in range(len(word1)):
            ans += word1[i]
            ans += word2[i]
        
        ans += extra
        return ans


        