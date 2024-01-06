class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0 , len(nums) - 1 # left and right pointers
        res = 0
        while l < r:
            if nums[l] + nums[r] == k:
                res += 1
                l += 1
                r -= 1

            elif nums[l] + nums[r] < k:
                l += 1
            elif nums[l] + nums[r] > k:
                r -= 1

        return res
        