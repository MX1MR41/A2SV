from math import sqrt

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        # sorting + dp
        
        nums.sort()
        dp = defaultdict(int)
        ans = 0

        for num in nums:
            root = sqrt(num)

            if root in dp:
                dp[num] = 1 + dp[root]
            else:
                dp[num] = 1

            ans = max(ans, dp[num])


        if ans < 2:
            return -1

        else:
            return ans


                
