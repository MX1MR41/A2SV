class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # bit manipulation + counting
        # the greatest AND will always be the greatest num in nums,
        # so the longest subarray with the biggest and will just be the longest consecutive
        # occurences of max(nums) in nums
        max_and = max(nums)

        count = 0
        res = 0

        for i in nums:
            if i == max_and:
                count += 1
            else:
                count = 0

            res = max(res, count)

        return res

            

