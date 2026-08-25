class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [-1 for _ in range(n)]
        dp[0] = 0
        for i in range(1, n):
            for j in range(i):
                if dp[j] == -1:
                    continue

                if abs(nums[i] - nums[j]) <= target:
                    dp[i] = max(dp[i], dp[j] + 1)



        return dp[-1] 
        
