class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = nums[:]
        for i in range(n):
            ind = (i + nums[i]) % n
            res[i] = nums[ind]

        return res

        
