class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # modified code from max consecutive-ones-iii
        # https://leetcode.com/problems/max-consecutive-ones-iii/
        res = 0
        n = len(nums)
        l, z = 0, 0 
        k = 1

        for r in range(n):
            if nums[r] != 1:
                z += 1
            while z > k:
                if nums[l] != 1:
                    z -= 1
                l += 1

            res = max(res, r-l)

        return res
        
        