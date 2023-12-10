class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count = {i: 0 for i in range(len(nums) + 1)}
        for i in nums:
            count[i] += 1

        for key, value in count.items():
            if value == 0:
                return key

        