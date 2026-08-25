class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        n = len(nums)
        l, z = 0, 0 

        for r in range(n):
            if not nums[r]:
                z += 1
            while z > k:
                if not nums[l]:
                    z -= 1
                l += 1

            res = max(res, r-l + 1)

        return res
        