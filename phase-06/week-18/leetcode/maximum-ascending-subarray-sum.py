class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = max(nums)
        pre = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                pre = 0

            pre += nums[i]

            res = max(res, pre)

        return res
        
