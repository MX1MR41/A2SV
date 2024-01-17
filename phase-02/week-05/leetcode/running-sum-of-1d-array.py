class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        presum = 0

        for i in nums:
            presum += i
            res.append(presum)

        return res
