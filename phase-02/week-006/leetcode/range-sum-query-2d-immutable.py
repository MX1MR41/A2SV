class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat = matrix
        m, n = len(self.mat), len(self.mat[0])
        self.psumrow = [[0 for i in range(n)] for j in range(m)]

        # a custom matrix that store prefixsum horizontally
        for i in range(m):
            psum = 0
            for j in range(n):
                psum += self.mat[i][j]
                self.psumrow[i][j] = psum



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        psum = 0
        m, n = len(self.mat), len(self.mat[0])
        for i in range(row1, row2 + 1):
            if col1 == col2:
                psum += self.mat[i][col1]
            elif not col1:
                psum += self.psumrow[i][col2]
            else:
                psum += self.psumrow[i][col2] - self.psumrow[i][col1-1]

        return psum
        