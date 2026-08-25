class Solution:
    def rob(self, nums: List[int]) -> int:
        # since the maximized way of robbing all houses is to do it alternatively,
        # when you are at a certain index i, the most amount of money you could have
        # is the largest from either the total you got from (i-1)th or 
        # or (i-2)th + nums[i]. Same for all i's until 0 and 1 for which are
        # nums[0] and max(nums[0], nums[1]) respectively
        n = len(nums)
        dp = defaultdict(int)
        dp[0] = nums[0]
        dp[1] = max(nums[:2])
        
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return max(dp[n], dp[n-1])
        
