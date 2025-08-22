class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        min_row = m
        min_col = n
        max_row = 0
        max_col = 0

        one = False

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    one = True
                    min_row = min(min_row, i)
                    min_col = min(min_col, j)
                    max_row = max(max_row, i)
                    max_col = max(max_col, j)


        if not one:
            return 0

        return (max_row - min_row + 1) * (max_col - min_col + 1)


        
        
