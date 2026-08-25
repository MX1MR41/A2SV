class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        return not any([count % 2 for count in Counter(nums).values()])
