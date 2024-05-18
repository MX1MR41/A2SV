class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # backtarking + dp + bit manipulation
        # we try various combinations of the numbers and keep track of
        # the used numbers using a bitmask
        mask = unmask = 0
        for i in range(len(nums)):
            unmask |= 1 << i
            
        dp = defaultdict(bool)

        target = sum(nums) / k # the sum of each subset 
        
        if target % int(target): return False # invalid partitioning

        def dfs(mask, part, tot):

            if mask in dp: # done and memoized already some subtree back left
                return dp[mask]
            if part > k or tot > target: # invalid partition
                return False
            if part == k and mask == unmask and tot == target: # validated
                dp[mask] = True
                return True

            if tot == target: # a new subset needs to be formed
                part += 1
                tot = 0

            for i in range(len(nums)):
                if not mask & (1 << i): # nums[i] hasn't been used down this subtree
                    temp = dfs(mask | (1 << i), part, tot + nums[i])
                    if temp: # break immediately, no need to search anymore
                        dp[mask] = True
                        return True

            dp[mask] = False

        return dfs(mask, 1, 0)
