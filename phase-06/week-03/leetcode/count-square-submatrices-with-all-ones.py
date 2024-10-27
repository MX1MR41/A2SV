class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # prefix sum over matrix
        # create a prefix sum matrix where a cell at (i,j) = sum of elements from (0,0) to (i,j).
        # To accumulate the sum at (i,j) you need to add the upper sum from (i-1, j) and left (i, j-1) 
        # then deduct diag (i-1, j-1) to mitigate the double counting since it is in both previous sums.
        # To figure out the sum from (p, q) to (i, j), do the reverse i.e. add the diagonal sum and
        # deduct the upper and left sums.
        
        pre = matrix[::]
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):
                up = pre[i-1][j] if i > 0 else 0
                left = pre[i][j-1] if j > 0 else 0
                diag = pre[i-1][j-1] if i > 0 and j > 0 else 0
                pre[i][j] = matrix[i][j] + up + left - diag

        count = 0


        for i in range(m):
            for j in range(n):
                prefix_sum = pre[i][j]

                p, q = i - 1, j - 1

                while p >= -1 or q >= -1:
                    up = pre[p][j] if p >= 0 else 0
                    left = pre[i][q] if q >= 0 else 0
                    diag = pre[p][q] if p >= 0 and q >= 0 else 0

                    net = prefix_sum - up - left + diag

                    if net == (i - p) * (j - q):
                        count += 1

                    p -= 1
                    q -= 1



        return count

        
