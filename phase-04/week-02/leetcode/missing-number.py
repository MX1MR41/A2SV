class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(n+1)

        for i in range(n):
            num = nums[i]
            while nums[i] != i and nums[num] != num:
                nums[i], nums[num] = nums[num], nums[i]

        res = set([i for i in range(n+1)])

        for i in nums:
            res.discard(i)

        return res.pop()

        