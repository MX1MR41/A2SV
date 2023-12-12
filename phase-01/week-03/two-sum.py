class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for ind, i in enumerate(nums):
            second =  target - nums[ind]
            if second in seen:
                return [ind, seen[second]]
            else:
                seen[i] = ind
        

    