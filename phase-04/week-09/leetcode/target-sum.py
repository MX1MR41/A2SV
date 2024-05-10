class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # DP: pruned backtracking
        # when drawing the recursion tree, we can see that we are repeatedly
        # calculating for some states (ind, tot). So instead of that, we can store their answer
        
        dp = defaultdict(int)
        n = len(nums)
        def dfs(ind, tot):
            if ind == n:
                if tot == target:
                    return 1
                return 0

            if (ind, tot) in dp:
                return dp[(ind, tot)]

            curr = 0

            curr += dfs(ind+1, tot + nums[ind]) 
            curr += dfs(ind+1, tot - nums[ind]) 

            dp[(ind, tot)] = curr

            return dp[(ind, tot)]

        return dfs(0,0)

                





            
        
