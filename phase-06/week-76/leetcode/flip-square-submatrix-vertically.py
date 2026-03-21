class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:

        for j in range(y, y + k):
            l = x
            r = x + k - 1

            while l < r:
                grid[l][j], grid[r][j] = grid[r][j], grid[l][j]

                l += 1
                r -= 1

        return grid
        
