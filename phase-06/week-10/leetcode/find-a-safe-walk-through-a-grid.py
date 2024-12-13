class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        if grid[0][0] >= health + 1:
            return False

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(grid), len(grid[0])
        valid = lambda i, j: 0 <= i < m and 0 <= j < n

        heap = [(-(health - grid[0][0]), (0, 0))]
        best = {}

        while heap:
            h, (i, j) = heappop(heap)
            h *= -1

            if (i, j) == (m - 1, n - 1):
                return True

            if h <= best.get((i, j), -1):
                continue

            best[(i, j)] = h

            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if valid(ni, nj):
                    nh = h - grid[ni][nj]
                    if nh > 0 and nh > best.get((ni, nj), -1):
                        heappush(heap, (-nh, (ni, nj)))

        return False
