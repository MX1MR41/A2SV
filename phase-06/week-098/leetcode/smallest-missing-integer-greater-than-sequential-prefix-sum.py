class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        seen = set(nums)
        
        summ = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                break

            summ += nums[i]

        maxx = summ
        while maxx in seen:
            maxx += 1

        return maxx

        
