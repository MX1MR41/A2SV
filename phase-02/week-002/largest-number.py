class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]

        def custom_sort(x):
            return x * 10

        nums.sort(key=custom_sort, reverse=True)

        if nums[0] == "0":
            return "0"

        return "".join(nums)
