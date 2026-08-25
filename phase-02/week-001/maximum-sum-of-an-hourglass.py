class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        ans, sum = 0, 0
        m, n = len(grid), len(grid[0])

        for i in range(m-2):
            for j in range(n-2):
                sum = grid[i][j] + grid[i][j+1] + grid[i][j+2]
                sum += grid[i+1][j+1]
                sum += grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]

                ans = max(sum, ans)

        return ans
