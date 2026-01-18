class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        # prefix sum over matrices in four direction
        m, n = len(grid), len(grid[0])

        down = [row[:] for row in grid]
        left = [row[:] for row in grid]
        diag1 = [row[:] for row in grid]
        diag2 = [row[:] for row in grid]

        for i in range(m):
            for j in range(1, n):
                left[i][j] += left[i][j - 1]

        for j in range(n):
            for i in range(1, m):
                down[i][j] += down[i - 1][j]

        for i in range(1, m):
            for j in range(1, n):
                diag1[i][j] += diag1[i - 1][j - 1]

        for i in range(1, m):
            for j in range(n - 2, -1, -1):
                diag2[i][j] += diag2[i - 1][j + 1]

        def check(i, j, i2, j2):
            summ = left[i][j] - left[i][j2 - 1] if j2 > 0 else left[i][j]

            for row in range(i2, i + 1):
                curr_sum = left[row][j] - left[row][j2 - 1] if j2 > 0 else left[row][j]

                if curr_sum != summ:
                    return False

            for col in range(j2, j + 1):
                curr_sum = down[i][col] - down[i2 - 1][col] if i2 > 0 else down[i][col]

                if curr_sum != summ:
                    return False

            d1 = (
                diag1[i][j] - diag1[i2 - 1][j2 - 1]
                if (i2 > 0 and j2 > 0)
                else diag1[i][j]
            )

            if d1 != summ:
                return False

            d2 = (
                diag2[i][j2] - diag2[i2 - 1][j + 1]
                if (i2 > 0 and j < n - 1)
                else diag2[i][j2]
            )

            if d2 != summ:
                return False

            return True

        res = 1
        for i in range(m):
            for j in range(n):

                steps = min(i, j)
                for step in range(1, steps + 1):
                    i2, j2 = i - step, j - step

                    if check(i, j, i2, j2):
                        res = max(res, i - i2 + 1)

        return res
