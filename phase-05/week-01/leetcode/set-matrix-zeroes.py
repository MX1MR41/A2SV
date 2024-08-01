class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        colzero, rowzero = set(), set()
        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    colzero.add(j)
                    rowzero.add(i)


        for i in range(m):
            for j in range(n):
                if i in rowzero or j in colzero:
                    matrix[i][j] = 0

                
        
