class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        # greedy
        # just keep taking as much zeros as you can
        # and take ones if an only if the resultant subsequence <= k

        res = ""

        for i in range(len(s) -1, -1, -1):
            if s[i] == "0":
                res = "0" + res
                continue
            
            if int("1" + res, 2) > k:
                continue
            
            res = "1" + res

        return len(res)

        
