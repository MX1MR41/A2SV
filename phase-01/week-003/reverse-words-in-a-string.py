class Solution:
    def reverseWords(self, s: str) -> str:
        words = list(s.split())
        ans = ""

        for i in reversed(range(len(words))):
            ans += words[i] + " "


        return ans.strip()        