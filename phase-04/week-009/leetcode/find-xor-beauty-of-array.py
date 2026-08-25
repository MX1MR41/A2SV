class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        # XOR magic
        # simplifying the expanded equation will yield just the XOR of the elements
        ans = 0
        for i in nums:
            ans ^= i

        return ans
        
