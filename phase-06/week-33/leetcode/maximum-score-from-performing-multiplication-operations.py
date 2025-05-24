class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # top down dp
        
        dp = {}

        n, m = len(nums), len(multipliers)
        def dfs(l, r, i):
            if (l, r) in dp:
                return dp[(l, r)]

            if i == m:
                return 0

            
            left = (multipliers[i] * nums[l]) + dfs(l + 1, r, i + 1)
            right = (multipliers[i] * nums[r]) + dfs(l, r - 1, i + 1)

            dp[(l, r)] = max(left, right)

            return dp[(l, r)]

        return dfs(0, n - 1, 0)
