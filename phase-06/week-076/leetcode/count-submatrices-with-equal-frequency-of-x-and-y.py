class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        freq_right = [[[0 for _ in range(2)] for _ in range(n)] for _ in range(m)]

        count = 0

        for i in range(m):
            for j in range(n):

                if grid[i][j] == "X":
                    freq_right[i][j][0] += 1
                elif grid[i][j] == "Y":
                    freq_right[i][j][1] += 1

                up = freq_right[i - 1][j] if i > 0 else [0, 0]
                left = freq_right[i][j - 1] if j > 0 else [0, 0]
                diag = freq_right[i - 1][j - 1] if i > 0 and j > 0 else [0, 0]

                freq_right[i][j][0] += up[0] + left[0] - diag[0]
                freq_right[i][j][1] += up[1] + left[1] - diag[1]

                if freq_right[i][j][0] > 0 and  freq_right[i][j][0] == freq_right[i][j][1]:
                    count += 1


        return count

        
