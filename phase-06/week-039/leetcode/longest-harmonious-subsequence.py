class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        res = 0

        l = 0

        n = len(nums)

        for r in range(n):
            if nums[r] - nums[l] < 1:
                continue

            while nums[r] - nums[l] > 1:
                l += 1

            if nums[r] - nums[l] == 1:
                res = max(res, r - l + 1)

        return res
        
