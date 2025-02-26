class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # prefix sum with kadane's approach
        # two passes: 1 to get the maximum positive sum, the other to get minimum neg sum
        res = 0
        pre = 0
        for i in nums:
            pre += i
            res = max(res, abs(pre))
            if pre < 0:
                pre = 0

        pre = 0
        for i in nums:
            pre += i
            res = max(res, abs(pre))
            if pre > 0:
                pre = 0

        return res
        
