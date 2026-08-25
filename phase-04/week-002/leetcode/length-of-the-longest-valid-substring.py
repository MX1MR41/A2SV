class Solution:
    def longestValidSubstring(self, word: str, forbidden: list[str]) -> int:
        forbidden_set = set(forbidden)
        res = start = 0
      
        for r in range(len(word)):
            for l in reversed(range(max(r - 10, start - 1), r + 1)):  
                if word[l:r + 1] in forbidden_set:
                    start = l + 1
                    break
          
            res = max(res, r - start + 1)
      
        return res
