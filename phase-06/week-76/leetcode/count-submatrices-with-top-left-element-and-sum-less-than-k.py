class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        pre = [[0 for _ in range(n)] for _ in range(m)]

        res = 0

        for i in range(m):
            for j in range(n):

                up = pre[i - 1][j] if i > 0 else 0
                left = pre[i][j - 1] if j > 0 else 0

                diag = pre[i - 1][j - 1] if i > 0 and j > 0 else 0

                pre[i][j] = grid[i][j] + up + left - diag

                if pre[i][j] <= k:
                    res += 1

        return res






        
