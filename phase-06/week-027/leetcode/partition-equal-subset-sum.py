class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # dp
        # To see if nums can be partitioned into two equal sum subsets, 
        # the sum of the subsets should be equal to sum(nums)//2.
        # So, it suffices for us to check if we can somehow form sum(nums)//2 by choosing
        # some (not all) numbers from nums, in which case, the remaining nums would also 
        # sum up to be sum(nums) - sum(nums)//2 which is equal to sum(nums)//2.
        # Hence the problem has become a knapsack problem where the target is sum(nums)//2.
        # Use a 1-D array dp of size sum(nums)//2, where dp[x] is True if x can be formed
        # by some choice of numbers from nums

        total = sum(nums)

        if total % 2:
            return False

        subset_sum = total // 2

        dp = [False] * (subset_sum + 1)

        n = len(nums)

        for num in nums:

            if num > subset_sum:
                continue

            # if we iterated forwards, we might double-count a single num's contributions
            # therefore we start from the right bigger sums so that sum2 + num wouldn't
            # overlap with sum1 + num where sum1 < sum2; process sum2 before sum1
            for curr_sum in range(subset_sum, -1, -1):
                if dp[curr_sum]:
                    new_sum = curr_sum + num

                    if new_sum <= subset_sum:
                        dp[new_sum] = True

            dp[num] = True

        return dp[subset_sum]
