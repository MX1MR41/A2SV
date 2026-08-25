class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        # pure dynamic programming
        # where the best value for (i, j) depends on its previous neighbours
        # (i-1, j) (i, j-1) (i-1, j-1)
        m = len(nums1)
        n = len(nums2)

        dp = [[float("-inf") for _ in range(n)] for _ in range(m)]
        
        for i in range(m):

            for j in range(n):

                prev_i = i - 1
                prev_j = j - 1

                dp[i][j] = nums1[i] * nums2[j]
                if prev_i >= 0 and prev_j >= 0:
                    dp[i][j] = max(dp[i][j], dp[i][j] + dp[prev_i][prev_j])
                    dp[i][j] = max(dp[i][j], dp[prev_i][prev_j])

                if prev_i >= 0:
                    dp[i][j] = max(dp[i][j], dp[prev_i][j])

                if prev_j >= 0:
                    dp[i][j] = max(dp[i][j], dp[i][prev_j])



        return dp[-1][-1]

        
