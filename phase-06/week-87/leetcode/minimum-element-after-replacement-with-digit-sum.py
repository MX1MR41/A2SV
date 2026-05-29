class Solution:
    def minElement(self, nums: List[int]) -> int:
        return min([sum(int(i) for i in str(num)) for num in nums])
