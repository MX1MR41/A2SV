class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        # sliding window
        res = 0

        freq = Counter()

        l = 0
        n = len(nums)
        for r in range(n):
            rnum = nums[r]
            freq[rnum] += 1

            while freq[rnum] > k:
                lnum = nums[l]
                freq[lnum] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
        
