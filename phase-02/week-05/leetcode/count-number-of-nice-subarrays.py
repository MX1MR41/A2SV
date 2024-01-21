class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # the number of odds, the final result, count of nice and left pointer respectively
        odd = res = curr = l = 0 
        for r in range(n):
            if nums[r] % 2:
                odd += 1
                curr = 0 # resetting it so we can restart counting all inclusive nice subs
                
            while odd == k:
                if nums[l] % 2:
                    odd -= 1

                curr += 1
                l += 1

            res += curr # adding the cumulative nice subs we found

        return res