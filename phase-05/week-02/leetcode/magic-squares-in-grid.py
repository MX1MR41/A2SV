from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def isMagic(rstart, cstart):
            s = {grid[rstart + i][cstart + j] for i in range(3) for j in range(3)}
            if s != {1, 2, 3, 4, 5, 6, 7, 8, 9}:
                return False

            r1 = sum(grid[rstart][cstart:cstart + 3])
            if sum(grid[rstart + 1][cstart:cstart + 3]) != r1:
                return False
            if sum(grid[rstart + 2][cstart:cstart + 3]) != r1:
                return False
            if sum(grid[rstart + i][cstart] for i in range(3)) != r1:
                return False
            if sum(grid[rstart + i][cstart + 1] for i in range(3)) != r1:
                return False
            if sum(grid[rstart + i][cstart + 2] for i in range(3)) != r1:
                return False
            if sum(grid[rstart + i][cstart + i] for i in range(3)) != r1:
                return False
            if sum(grid[rstart + i][cstart + 2 - i] for i in range(3)) != r1:
                return False

            return True

        grids = 0
        for r in range(m - 2):
            for c in range(n - 2):
                if isMagic(r, c):
                    grids += 1

        return grids
