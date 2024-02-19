class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        # this approach aims at evenly dividing the already seen total
        # or prefix sum among the number of elements seen so far
        # that way we can get the most optimal value of the minimization of the max
        res = pre = nums[0]
        n = len(nums)

        for i in range(1,n):
            pre += nums[i]
            res = max(res, ceil(pre/(i+1)))

        return res
        