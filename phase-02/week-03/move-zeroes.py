class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        z , n = 0, 0 # index of leftmost zeroth index and non-zero index resp...
        l = len(nums)
        while z < l and n < l:
            while z < n and nums[z]: # if nums[z] is non-zero
                z += 1

            if nums[n]: # if nums[n] is non-zero, else we'll increment to find 
                nums[z], nums[n] = nums[n], nums[z]
                z += 1

            n += 1
