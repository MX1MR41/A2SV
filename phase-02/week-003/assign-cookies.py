class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ans = 0
        n1, n2 = len(g), len(s)
        i , j = 0, 0

        while i < n1 and j < n2:
            a, b = g[i], s[j] # current child and cookie 

            if b >= a:
                ans += 1
                i += 1
                j += 1

            else:
                j += 1


        return ans

        