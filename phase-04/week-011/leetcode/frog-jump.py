class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # bottom-up dp
        # it is possible to reach a stone from various stones and various jumps k
        # so dp[stone] will store the jumps that could reach stone.
        # when we reach that stone, we compute for (stone + k), (stone + k + 1)
        # and (stone + k + 1) and add their respective jumps into their dp
        dp = defaultdict(set)
        k = stones[1] - stones[0]
        if k > 1: return False # we can't even reach the second stone

        dp[stones[1]].add(k)
        # base case: the second stone
        dp[stones[1] + k].add(k)
        dp[stones[1] + k - 1].add(k-1)
        dp[stones[1] + k + 1].add(k+1)

        for stone in stones[2:]:
            if dp[stone]: # was possible to reach this stone from some jump earlier
                ks = list(dp[stone]) # list of jumps that reached this stone
                for k in ks:
                    dp[stone + k].add(k)
                    dp[stone + k - 1].add(k-1)
                    dp[stone + k + 1].add(k+1)

        return True if dp[stones[-1]] else False



        
