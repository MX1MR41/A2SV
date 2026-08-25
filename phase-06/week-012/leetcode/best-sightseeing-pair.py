class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = 0
        prev_max = 0
  
        for index, value in enumerate(values):
            ans = max(ans, value - index + prev_max)
            prev_max = max(prev_max, index + value)

        return ans        
