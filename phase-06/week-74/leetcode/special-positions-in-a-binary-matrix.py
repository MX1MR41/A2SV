class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        right = [m[:] for m in mat]
        down = [m[:] for m in mat]
        
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(1, n):
                right[i][j] += right[i][j - 1]

        for j in range(n):
            for i in range(1, m):
                down[i][j] += down[i - 1][j]

        res = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    continue

                if right[i][-1] == 1 and down[-1][j] == 1:
                    res += 1

        return res
