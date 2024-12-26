class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dp
        # build up the sum from the first index in a bottom-up manner
        # and store the count of each sum as a map of sums in a map of indices
        # TC = O(N) because inner loop runs for maximum of difference between
        # -sum(nums[:index]) upto sum(nums[:index]) which is near constant
        dp = defaultdict(lambda: defaultdict(int))

        dp[0][nums[0]] += 1
        dp[0][-nums[0]] += 1

        for i in range(1, len(nums)):

            for j in dp[i - 1]:
                dp[i][j + nums[i]] += dp[i - 1][j]
                dp[i][j - nums[i]] += dp[i - 1][j]

        return dp[len(nums) - 1][target]
