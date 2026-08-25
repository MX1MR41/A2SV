class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        nums = []
        cost = 0

        for i in instructions:
            n = len(nums)
            insertPoint = bisect_left(nums,i)
            nums.insert(insertPoint, i)
            end = bisect_right(nums, i) - 1
            cost += min(insertPoint, len(nums) - (end + 1)) 

        mod = 1000000007
        return cost % mod
        