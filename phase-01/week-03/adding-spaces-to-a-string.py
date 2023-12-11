class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ""
        j = 0
        for i in spaces:

            ans += s[j:i] + " "

            j = i

        ans += s[spaces.pop():]


        return ans

        