class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        # dp
        # quadratic algorithm where for every index, we iterate over every prev
        # index and compuute the maximum length of sub ending at the current index

        n = len(nums)

        dp = [[-1 for _ in range(k)] for _ in range(n)]

        dp[0]

        res = 0

        for i in range(1, n):
            curr = nums[i]
            for j in range(i):
                prev = nums[j]
                modulo = (prev + curr) % k

                if dp[j][modulo] == -1: # no
                    dp[i][modulo] = max(dp[i][modulo], 2)
                else:
                    dp[i][modulo] = max(dp[i][modulo], dp[j][modulo] + 1)

            res = max(res, max(dp[i]))

        return res


        
