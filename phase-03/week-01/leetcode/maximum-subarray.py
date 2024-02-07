class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadane's approach
        res = curr = float("-inf")
        n = len(nums)
        for i in nums:
            if curr < 0:
                curr = 0
            curr += i

            res = max(res, curr)

        return res
        
        