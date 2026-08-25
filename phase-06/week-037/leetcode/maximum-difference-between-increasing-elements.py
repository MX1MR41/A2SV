class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        minn = float("inf")
        res = -1

        for i in range(len(nums)):
            if minn < nums[i]:
                res = max(res, nums[i] - minn)
            minn = min(minn, nums[i])

        return res
