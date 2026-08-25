class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        def inbound(r, c):
            return 0 <= r < M and 0 <= c < N

        def dfs(r, c):
            if not inbound(r, c) or not grid[r][c]:
                return 1  # Return 1 for water or out-of-bounds cells

            if grid[r][c] == -1:  # Mark visited cells to avoid double counting
                return 0

            grid[r][c] = -1  # Mark the cell as visited

            perimeter = 0
            perimeter += dfs(r - 1, c)
            perimeter += dfs(r + 1, c)
            perimeter += dfs(r, c - 1)
            perimeter += dfs(r, c + 1)

            return perimeter

        total_perimeter = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    total_perimeter += dfs(i, j)

        return total_perimeter
