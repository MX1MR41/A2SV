class Solution:
    def maxSum(self, nums: List[int]) -> int:

        res = float("-inf")

        n = len(nums)

        for l in range(n):
            for r in range(l + 1, n + 1):
                unique = set(nums[l:r])
                if max(unique) <= 0:
                    res = max(res, max(unique))
                    continue

                res = max(res, sum(i for i in unique if i >= 0))

        return res
