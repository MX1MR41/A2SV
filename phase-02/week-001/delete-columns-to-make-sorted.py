class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m = len(strs)
        n = len(strs[0])
        ans = 0

        temp = [[0] * m for i in range(n)]

        for i in range(m):
            for j in range(n):
                temp[j][i] = strs[i][j]

        for s in temp:
            if s != sorted(s):
                ans += 1

        return ans




        