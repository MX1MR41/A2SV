class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        # sliding window + dp
        n = len(nums)
        dp = [1] * n

        l = 0
        for r in range(1, n):
            if nums[r] <= nums[r - 1]:
                l = r
                continue

            dp[r] = r - l + 1

        for i in range(k, n):
            if dp[i] >= k:
                if dp[i - k] >= k:
                    return True


        return False

