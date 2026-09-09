class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        r, c = 0, n - 1

        while 0 <= r < m and 0 <= c < n:
            if matrix[r][c] == target:
                return True

            if matrix[r][c] > target:
                c -= 1

            elif matrix[r][c] < target:
                r += 1


        return False
        
