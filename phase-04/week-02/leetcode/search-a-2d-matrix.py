class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # math + binary search
        # order the cells from 0 to m*n - 1 going from left to right and top to bottom
        # do binary seacrh to get the target

        def getkthcell(k, m, n):
            row = k//n
            col = k - (row)*n
            return matrix[row][col]

        m, n = len(matrix), len(matrix[0])

        left, right = 0, m*n - 1


        while left <= right:
            mid = (left + right)//2
            cell = getkthcell(mid, m, n)
            if cell == target:
                return True

            if cell < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
            
        
