class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        # dp
        # two possible sets of peaks, we run the dp for both
        n = len(nums)
        if k == 0:
            return 0

        if k > n // 2:
            return -1

        costs = [0] * n
        for i in range(n):
            left, num, right = nums[(i - 1) % n], nums[i], nums[(i + 1) % n]
            if left < num > right:
                costs[i] = 0
            else:
                costs[i] = max(right - num + 1, left - num + 1)

        def run_dp_on_straight_line(start_idx, end_idx):
            length = end_idx - start_idx
            if length < 1:
                return float("inf")

            dp = [[float("inf") for _ in range(k)] for _ in range(length)]

            for i in range(length):
                real_i = start_idx + i
                min_ops = costs[real_i]

                dp_curr = dp[i]

                dp_imm_prev = dp[i - 1] if i - 1 >= 0 else [float("inf")] * k
                dp_prev = dp[i - 2] if i - 2 >= 0 else [float("inf")] * k

                dp_curr[0] = min(dp_prev[0], dp_imm_prev[0], min_ops)

                for j in range(1, k):
                    dp_curr[j] = min(min_ops + dp_prev[j - 1], dp_imm_prev[j])

            return dp[-1][-1]

        ans1 = run_dp_on_straight_line(0, n - 1)

        ans2 = run_dp_on_straight_line(1, n)

        return min(ans1, ans2)
