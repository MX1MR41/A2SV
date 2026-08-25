class Solution:
    def maxSum(self, nums: List[int]) -> int:


        negs = [num for num in nums if num <= 0]

        res = max(negs) if negs else 0

        unique = set([num for num in nums if num > 0])
        if unique:
            res = max(res, sum(unique))

        return res
