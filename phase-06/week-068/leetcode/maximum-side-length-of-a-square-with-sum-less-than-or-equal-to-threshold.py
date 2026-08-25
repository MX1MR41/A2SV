class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        # prefix sum + binary search

        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                up = mat[i - 1][j] if i > 0 else 0
                left = mat[i][j - 1] if j > 0 else 0
                diag = mat[i - 1][j - 1] if (i > 0 and j > 0) else 0

                mat[i][j] += up + left - diag

        


        def check(size):
            for i in range(size - 1, m):

                for j in range(size - 1, n):

                    up = mat[i - size][j] if i - size > 0 else 0
                    left = mat[i][j - size] if j - size > 0 else 0
                    diag = (
                        mat[i - size][j - size] 
                        if (i - size > 0 and j - size > 0)
                        else 0
                    )

                    square_sum = mat[i][j] - up - left + diag
                    if square_sum <= threshold:
                        return True

            return False

                    



        l, r = 0, min(m, n)
        res = 0

        while l <= r:
            mid = (l + r)//2
            if check(mid):
                res = mid
                l = mid + 1
            else:
                r = mid - 1

        return res
        
