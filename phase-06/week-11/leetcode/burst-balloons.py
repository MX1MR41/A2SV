class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # dp
        # instead of bursting a balloon first, think on bursting a balloon last
        # then compute in a bottom up manner what the optimal solution would be
        # for every size subarray starting from size 1 then 2 then 3 ...
        
        # Step 1: Add virtual balloons with value 1 at the ends
        nums = [1] + nums + [1]
        n = len(nums)
        
        # Step 2: Create a DP table initialized to 0
        dp = [[0] * n for _ in range(n)]
        
        # Step 3: Bottom-up DP - iterate over subarray lengths
        for length in range(1, n - 1):  # length of the subarray [left, right]
            for left in range(1, n - length):  # left boundary
                right = left + length - 1  # right boundary
                
                # Step 4: Burst balloons within range [left, right]
                for k in range(left, right + 1):  # k is the last balloon to burst
                    coins = (
                        nums[left - 1] * nums[k] * nums[right + 1]  # Coins for bursting k last
                        + dp[left][k - 1]  # Max coins from left subarray
                        + dp[k + 1][right]  # Max coins from right subarray
                    )
                    dp[left][right] = max(dp[left][right], coins)  # Update DP table

        # Step 5: Result is stored in dp[1][n-2]
        return max([max(d) for d in dp])
