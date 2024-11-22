class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # flipping columns of some array in the matrix will negatively affect
        # other arrays of different configuration, nut will positively affect
        # other arrays of the same configuration
        # configuration as in which indices of the array have the same elements 
        # e.g. [0,1,0,0,1] has both configurations (0,2,3) and (1,4)
        # the answer will be the maximum number of arrays that have similar configs
        
        count = defaultdict(int)
        m, n = len(matrix), len(matrix[0])
        for mat in matrix:
            ones, zeros = [], []
            for i in range(n):
                if mat[i] == 1:
                    ones.append(i)
                else:
                    zeros.append(i)

            count[tuple(ones)] += 1
            count[tuple(zeros)] += 1

        return max(count.values())
        
        
