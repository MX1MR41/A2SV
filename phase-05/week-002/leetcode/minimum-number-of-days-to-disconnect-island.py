class Solution:
    def minDays(self, grid: List[List[int]]) -> int:

        if self.count_islands(grid) != 1:
            return 0

        num_rows, num_cols = len(grid), len(grid[0])

        for row in range(num_rows):
            for col in range(num_cols):

                if grid[row][col] == 1:

                    grid[row][col] = 0

                    if self.count_islands(grid) != 1:
                        return 1

                    grid[row][col] = 1

        return 2

    def count_islands(self, grid: List[List[int]]) -> int:

        def dfs(row: int, col: int):
            grid[row][col] = 2

            directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]

            for delta_row, delta_col in directions:
                next_row, next_col = row + delta_row, col + delta_col

                if (
                    0 <= next_row < num_rows
                    and 0 <= next_col < num_cols
                    and grid[next_row][next_col] == 1
                ):
                    dfs(next_row, next_col)

        num_rows, num_cols = len(grid), len(grid[0])
        island_count = 0

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 1:
                    dfs(row, col)
                    island_count += 1

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 2:
                    grid[row][col] = 1

        return island_count
