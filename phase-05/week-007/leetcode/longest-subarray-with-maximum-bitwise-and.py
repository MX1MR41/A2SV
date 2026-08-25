class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # the maximum AND will always be the greatest number in the array
    
        ans = 1

        l = 0
        mx = max(nums)
        curr = nums[0]
        for r in range(len(nums)):
            curr &= nums[r]
            if curr != mx:
                curr = mx
                l = r + 1
            
            ans = max(ans, r - l + 1)

        return ans

        
