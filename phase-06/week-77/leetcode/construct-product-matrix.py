class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])

        p = [[0] * m for _ in range(n)]

        pref = 1
        for i in range(n):
            for j in range(m):
                p[i][j] = pref

                pref = (pref * grid[i][j]) % 12345

        suff = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                p[i][j] = (p[i][j] * suff) % 12345

                suff = (suff * grid[i][j]) % 12345

        return p
