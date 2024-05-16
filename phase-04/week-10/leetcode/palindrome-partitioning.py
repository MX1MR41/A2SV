class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def pal( s, l, r):
            while l < r:
                if s[l] != s[r]: return False
                l, r = l + 1, r - 1

            return True

        res, part = [], []

        def dfs(ind):
            if ind >= len(s):
                res.append(part[::])
                return
                
            for j in range(ind, len(s)):
                if pal(s, ind, j):
                    part.append(s[ind : j + 1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return res

