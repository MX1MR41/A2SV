class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        start = bisect_left(nums, target)
        
        if 0 <= start < len(nums) and nums[start] == target:
            start = start
        else:
            start = -1

        end = bisect_right(nums, target) - 1

        if 0 <= end < len(nums) and nums[end] == target:
            end = end
        else:
            end = -1

        return [start, end] 
        


            


        