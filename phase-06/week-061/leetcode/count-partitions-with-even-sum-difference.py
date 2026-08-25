class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        right = sum(nums)
        left = 0
        res = 0
        for num in nums[:-1]:
            left += num
            right -= num
            if (left - right) % 2 == 0:
                res += 1

        return res
            
        
