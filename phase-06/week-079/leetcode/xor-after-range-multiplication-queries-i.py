class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 1000000007
        for l, r, k, v in queries:
            for i in range(l, r + 1, k):
                nums[i] = (nums[i] * v) % MOD

        res = nums[0]
        for i in range(1, len(nums)):
            res ^= nums[i]

        return res
        
