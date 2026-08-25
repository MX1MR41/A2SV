class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        res = 0
        l = 0

        for r in range(len(nums)):
            if r - l + 1 < 3:
                continue

            if nums[r] + nums[l] == nums[r - 1]/2:
                res += 1

            l += 1

        return res
        
