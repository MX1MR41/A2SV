class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for i in range(2 * k - 1, n):
            yes = True

            for j in range(i - 1, i - k, -1):

                if nums[j] >= nums[j + 1]:
                    yes = False
                    break

            for j in range(i - k - 1, i - 2 * k, -1):

                if nums[j] >= nums[j + 1]:
                    yes = False
                    break

            if yes:

                return True

        return False
