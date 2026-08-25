class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        # sliding window
        # preprocess to find and store the greatest number to the right of each number
        # keep expanding window as long as the greatest number to the right is >= num at left of window
        max_right = []
        last_max = 0

        for i in reversed(range(len(nums))):
            if nums[i] > last_max:
                last_max = nums[i]
            max_right.append(last_max)

        max_right.reverse()

        l = ans = 0

        for r in range(len(nums)):
            if max_right[r] < nums[l]:
                l += 1

            ans = max(ans, r - l)


        return ans
        
