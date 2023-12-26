class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans, n = 0, len(mat)

        for i in range(n): # add the diag elems in the same row
            ans += mat[i][i]
            ans += mat[i][n-1-i]

        if n % 2: # if it is odd, we have added the center element twice, soo..
            ans -= mat[n//2][n//2]
        
        return ans

        


        