class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        m = max(nums)

        res = 0
        l = 0
        n = len(nums)
        freq = defaultdict(int)
        for r in range(n):
            rnum = nums[r]
            freq[rnum] += 1

            while freq[m] == k:
                res += n - r
                lnum = nums[l]
                freq[lnum] -= 1
                l += 1

        return res

        
