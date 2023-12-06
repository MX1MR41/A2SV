class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, r = 0, 0
        res = 0
        while r < len(nums):
            if nums[r] == 1:
                r += 1
                res = max(r - l, res)
            else:
                res = max(r - l, res)
                r += 1
                l = r

        return res

        
