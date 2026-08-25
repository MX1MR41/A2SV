class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # backtracking with dynamic programming pruninng
        dp = defaultdict(bool)
        tot = sum(nums)
        if tot % 2:
            return False
        half = tot >> 1
        n = len(nums)

        def dfs(ind, curr):
            if ind == n:
                return False
            if curr == half:
                return True

            if (ind, curr) in dp:
                return dp[(ind, curr)]

            dp[(ind, curr)] = dfs(ind + 1, curr + nums[ind]) or dfs(ind + 1, curr)
            return dp[(ind, curr)]

        return dfs(0, 0)
