class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        # XOR magic
        ans = 0
        for i in nums:
            ans ^= i

        return ans
        
