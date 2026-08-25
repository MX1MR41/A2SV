class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])

        inbound = lambda i, j: 0 <= i < m and 0 <= j < n

        clockwise = {
            (1, 1): (1, -1),
            (1, -1): (-1, -1),
            (-1, -1): (-1, 1),
            (-1, 1): (1, 1)

        }

        @lru_cache(None)
        def dfs(i, j, di, dj,turned):

            maxx = 0

            ni = i + di
            nj = j + dj

            if inbound(ni, nj) and grid[ni][nj] == abs(grid[i][j] - 2):
                temp = dfs(ni, nj, di, dj, turned)
                maxx = max(maxx, temp)

            if not turned:
                ndi, ndj = clockwise[(di, dj)]

                ni = i + ndi
                nj = j + ndj

                if inbound(ni, nj) and grid[ni][nj] == abs(grid[i][j] - 2):
                    temp = dfs(ni, nj, ndi, ndj, True)
                    maxx = max(maxx, temp)

            return maxx + 1


        res = 0

        dirs = [(1, 1), (-1, -1), (1, -1), (-1, 1)]

        for i in range(m):
            for j in range(n):

                if grid[i][j] != 1:
                    continue

                maxx = 0

                for di, dj in dirs:
                    ni = i + di
                    nj = j + dj
                    if inbound(ni, nj) and grid[ni][nj] == 2:
                        maxx = max(maxx, dfs(ni, nj, di, dj, False))

                res = max(res, maxx + 1)


        return res
