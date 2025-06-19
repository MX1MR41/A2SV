class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        # greedy + sorting

        nums.sort()

        left = right = 0
        n = len(nums)

        subs = 1
        while right < n:

            if nums[right] - nums[left] > k:
                subs += 1
                left = right

            else:
                right += 1

        return subs
