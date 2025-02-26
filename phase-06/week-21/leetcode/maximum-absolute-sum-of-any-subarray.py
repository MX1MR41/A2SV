class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # prefix sum with kadane's approach
        # keep track of the maximum positive sum and the minimum negative sum seen so far
        # use kadane's approach on the positive prefix sum and a modified kadane on neg sum
        res = 0
        pos = 0
        neg = 0
        for i in nums:
            pos += i
            neg += i
            res = max(res, abs(pos), abs(neg))
            if pos < 0:
                pos = 0
            if neg > 0:
                neg = 0

        return res
        
