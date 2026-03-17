class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        # prefix sum
        # count and sum up downwards the number of consecutive ones in a column
        # so that matrix[i][j] = the number of consecutive ones upto (i, j)
        # after to simulate the reordering of columns, we sort the rows in descending order
        # so that by the time we reach matrix[i][j] which has a value of x, 
        # we know that we have seen j + 1 columns to the left whose [i][j] values 
        # are greater than or equal to x, meaning we can form a rectangle of height x
        # and width (j + 1)
        m, n = len(matrix), len(matrix[0])
        for j in range(n):
            ones = 0
            for i in range(m):
                if matrix[i][j] == 0:
                    ones = 0

                matrix[i][j] += ones
                ones = matrix[i][j]


        for i in range(m):
            matrix[i].sort(reverse = True)

        res = 0

        for i in range(m):
            for j in range(n):
                curr = matrix[i][j] * (j + 1)

                res = max(res, curr)

        return res


                    
        
