class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        # greedy 
        # at each cell, we try to make it as large as possible
        # i.e. minimum of the remaining rowSum for that row and colSum for that col

        m, n = len(rowSum), len(colSum)
        mat = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):

                mat[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= mat[i][j]
                colSum[j] -= mat[i][j]


        return mat
