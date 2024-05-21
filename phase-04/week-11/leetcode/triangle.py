class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0]*j for j in range(1, n+1)]
        dp[0] = triangle[0]

        for i in range(1, n):
            curr = triangle[i]
            m = len(curr)
            for j in range(m):
                if j == 0:
                    left = float("inf")
                    right = dp[i-1][j]

                elif j == m-1:
                    right = float("inf")
                    left = dp[i-1][j-1]

                else:
                    left, right = dp[i-1][j-1], dp[i-1][j]

                dp[i][j] = triangle[i][j] + min(left, right)


        return min(dp[-1])

        
