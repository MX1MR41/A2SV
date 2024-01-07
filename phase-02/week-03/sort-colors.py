class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        l = 0
        while l < n-1  and nums[l] == 0: # find the leftmost nonzero element index
            l += 1
        # first, put all zeros to the left of the list
        r = l + 1 
        while r < n: # check if r is a 0, then swap
            if nums[r] == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1 # update the pos of the leftmost nonzero element index
            r += 1
        
        r = n - 1
        while r >= 1 and nums[r] == 2: # find the rightmost non-two element index
            r -= 1
        # now put all twos to the right of the list
        l = r - 1
        while l >= 0:
            if nums[l] == 2: # check if l is 2, then swap
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1 # update the pos of the rightmost non-two element index
            l -= 1


        