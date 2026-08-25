class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        # greedy
        ans = []
    
        for i, group_number in enumerate(groups):

            if i == 0 or group_number != groups[i - 1]:
    
                ans.append(words[i])
      
        return ans        
