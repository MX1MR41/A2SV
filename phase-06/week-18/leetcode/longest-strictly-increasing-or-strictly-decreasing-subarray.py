class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        dp1 = [1]*(n)
        dp2 = [1]*(n)

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                dp1[i] += dp1[i - 1]

        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                dp2[i] += dp2[i - 1]

        return max(max(dp1), max(dp2))



        
