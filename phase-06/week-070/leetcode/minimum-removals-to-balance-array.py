class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        # sliding window
        # instead of thinking which elements to remove, think of which elements to keep
        # sort the array and then find the largest subarray that satisfies conditions
        res = 0
        nums.sort()

        n = len(nums)
        l = 0
        for r in range(n):
            while nums[l] * k < nums[r]:
                l += 1

            res = max(res, r - l + 1)

        return n - res 
        
