class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # sliding window
        # each window slide deducts (total_sum - new_num) from the window and adds (n - 1) * new_num
        n = len(nums)
        tot = sum(nums)

        res = float("-inf")

        nums += nums

        window = 0

        l = 0
        for r in range(2*n):

            if r - l + 1 <= n:
                window += r * nums[r]
                continue

            curr_window = window - (tot - nums[r]) + (n - 1)*nums[r]
            res = max(res, curr_window)
            window = curr_window
            l += 1

        return res
