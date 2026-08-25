class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # bottom up dp
        # for each element, we check to see if the number whuch is element - diff
        # was seen before and if so we add that number's precomputed result onto
        # our current element
        dp = defaultdict(int)
        ans = 1

        for num in arr:

            prev = num - difference
            dp[num] = dp[prev] + 1
            ans = max(ans, dp[num])


        return ans
