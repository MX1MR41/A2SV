class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        res = 0

        l = 0
        summ = 0
        n = len(nums)
        for r in range(n):
            summ += nums[r]

            while l <= r and summ * (r - l + 1) >= k:
                summ -= nums[l]
                l += 1

            res += r - l + 1

        return res

        
