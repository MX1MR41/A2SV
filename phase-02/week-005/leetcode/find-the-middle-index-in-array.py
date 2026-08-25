class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        l, r, n = 0, sum(nums), len(nums)

        for i in range(n):
            num = nums[i]
            r -= num
            if l == r:
                return i

            l += num

        return -1
        