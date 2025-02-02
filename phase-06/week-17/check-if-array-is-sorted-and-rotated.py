class Solution:
    def check(self, nums: List[int]) -> bool:
        start = 0
        n = len(nums)
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                start = i
                break

        for i in range(1, n):
            num = nums[(start + i) % n]
            prev = nums[(start + i - 1) % n]
            if num < prev:
                return False

        return True
