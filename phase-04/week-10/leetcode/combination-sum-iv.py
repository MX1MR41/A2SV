class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        ans = 0
        dp = defaultdict(int)

        def dfs(tot):
            if tot in dp: return dp[tot]
            if tot > target: return 0
            if tot == target: return 1

            temp = 0
            for num in nums:
                temp += dfs(tot + num)

            dp[tot] = temp
            return temp
        return dfs(0)
        
