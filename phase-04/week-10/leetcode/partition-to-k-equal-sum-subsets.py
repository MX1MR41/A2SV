class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        mask = 0
        unmask = 0
        for i in range(len(nums)):
            unmask |= 1 << i
        dp = defaultdict(bool)
        target = sum(nums)/k
        if target % int(target): return False

        def dfs(mask, part, tot):

            if mask in dp: return dp[mask]
            if part > k or tot > target: return False
            if part == k and mask == unmask and tot == target:
                dp[mask] = True
                return True

            if tot == target: 
                part += 1
                tot = 0

            for i in range(len(nums)):
                if not mask & (1 << i):
                    temp = dfs(mask | (1 << i), part, tot + nums[i])
                    if temp:
                        dp[mask] = True
                        return True

            dp[mask] = False

        return dfs(mask, 1, 0)





            
                

        
