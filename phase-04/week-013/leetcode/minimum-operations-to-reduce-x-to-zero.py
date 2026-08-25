class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # sliding window
        # problem asks to find some chunks of the array from the left and from the right
        # whose total sum is equal to x, so that we can cancel out x.
        # since we are subtracting form either ends of the array, we will be left with
        # an untouched chunk (a window) in the middle. Hence problem can be reframed to 
        # find a window whose sum is equal to the total sum of the array minus the sum 
        # of removed chunks from either side whose value is x.
        tot = sum(nums)

        target = tot - x
        if target == 0: return len(nums)

        ans = 0
        l = 0
        window = 0
        for r in range(len(nums)):
            window += nums[r]
            while l < r and window > target:
                window -= nums[l]
                l += 1

            if window == target:
                ans = max(ans, r - l + 1)

        return len(nums) - ans if ans else -1

        
