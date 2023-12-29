class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        d, ans = {}, ""

        for i in range(len(s)):
            d[int(s[i][-1])] = s[i][:-1]

        print(d)

        for j in range(1, len(d)+1):
            ans += d[j] + " "

        ans = ans.rstrip()

        return ans
        