class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        n = len(nums) 
        l = 0 #left pointer
        curr = 0 # sliding window sum

        for r in range(n):
            curr += nums[r]

            if curr >= target:
                res = min(res, r-l +1)
                # shrink the window from the left
                while curr >= target and l <= r: 
                    curr -= nums[l]
                    l += 1
                # since l to r is the length of the sub with sum < target
                # we calculate the length that we just shrunk
                res = min(res, r-l+2) 


        return res if res != float("inf") else 0



        



        