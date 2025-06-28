class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        nums = [(num, ind) for ind, num in enumerate(nums)]
        nums.sort(key = lambda x: -x[0])
        return [x[0] for x in sorted(nums[:k], key = lambda x: x[1])]
        
