class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1, n2 = len(str1), len(str2)
        s1 = str1 if n1 <= n2 else str2
        s2 = str1 if s1 == str2 else str2

        n1, n2 = min(n1, n2), max(n1, n2)

        ans = ""
        for i in range(n1):
            for j in range(i + 1, n1 + 1):
                div = s1[i:j]

                times2 = n2//(j - i)
                times1 = n1//(j - i)
                if s2 == div * times2 and s1 == div * times1:
                    ans = max(ans, div, key = lambda x: len(x))

        return ans
        
