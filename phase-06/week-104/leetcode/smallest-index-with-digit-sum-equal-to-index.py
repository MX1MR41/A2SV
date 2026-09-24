class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if sum(list(map(int, list(str(nums[i]))))) == i:
                return i

        return -1
        
