class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        # dp
        # quadratic algorithm where for every index, we iterate over every prev
        # index and compuute the maximum length of sub ending at the current index

        n = len(nums)

        dp = [[-1 for _ in range(1002)] for _ in range(n)]

        dp[0]

        res = 0

        for i in range(1, n):
            curr = nums[i]
            for j in range(i):
                prev = nums[j]
                diff = curr - prev + 500
                if dp[j][diff] == -1:
                    dp[i][diff] = max(dp[i][diff], 2)
                else:
                    dp[i][diff] = max(dp[i][diff], dp[j][diff] + 1)

            res = max(res, max(dp[i]))

        return res


        
        
