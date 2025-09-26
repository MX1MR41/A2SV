class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # heap + bfs + dijkstra
        # performs a bfs using a heap where the top element is the cell that is reached with
        # the smallest amount of time
        # then expand from a cell, if the cell's height is greater than the current time of
        # the cell, we add the difference because we need to wait until the water level 
        # reaches as high as the neighbor cell's height

        heap = [(grid[0][0], 0, 0)]

        m, n = len(grid), len(grid[0])

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        inbound = lambda i, j: 0 <= i < m and 0 <= j < n
        seen = set()



        while heap:
            t, i, j = heappop(heap)
            if (i, j) == (m - 1, n - 1):
                return t

            if (i, j) in seen:
                continue

            seen.add((i, j))

            h = grid[i][j]

            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if inbound(ni, nj) and (ni, nj) not in seen:
                    nh = grid[ni][nj]
                    if t < nh:
                        nt = t + (nh - t)
                    else:
                        nt = t

                    heappush(heap, (nt, ni, nj))
