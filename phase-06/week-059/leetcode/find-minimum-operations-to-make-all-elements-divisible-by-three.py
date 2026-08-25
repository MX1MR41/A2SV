class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(min(abs(num - 3*floor(num/3)), abs(num - 3*ceil(num/3))) for num in nums)
        
