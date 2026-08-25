class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:

        m, n = len(mat), len(mat[0])

        horz = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            ones = 0
            for j in range(n):
                if mat[i][j] == 1:
                    ones += 1
                else:
                    ones = 0

                horz[i][j] = ones

        res = 0

        for i in range(m):
            
            for j in range(n):

                if mat[i][j] == 0:
                    continue

                min_width = horz[i][j]

                r = i
                while r >= 0 and mat[r][j] == 1:
                    min_width = min(min_width, horz[r][j])
                    res += min_width
                    r -= 1

        return res
