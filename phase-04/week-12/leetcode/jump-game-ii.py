class Solution:
    def jump(self, nums: List[int]) -> int:
        # bottom-up dp
        n = len(nums)
        dp = [float("inf")] * n
        dp[0] = 0
        for i in range(n):
            end = nums[i] + i
            for j in range(i+1, min(end+1, n)):
                dp[j] = min(dp[j], dp[i] + 1)

        return dp[-1]
        
