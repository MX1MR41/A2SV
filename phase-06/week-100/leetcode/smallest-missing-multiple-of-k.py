class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        res = k
        m = 1
        while m * k in nums:
            m += 1

        return m * k
        
