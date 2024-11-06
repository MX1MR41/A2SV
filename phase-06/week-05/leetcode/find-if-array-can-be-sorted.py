class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        ans = True

        n = len(nums)
        for i in range(n):
            for j in range(i):
                if nums[i] < nums[j]:
                    if nums[j].bit_count() != nums[i].bit_count():
                        ans = False


            for j in range(i + 1, n):
                if nums[j] < nums[i]:
                    if nums[j].bit_count() != nums[i].bit_count():
                        ans = False


        return ans
