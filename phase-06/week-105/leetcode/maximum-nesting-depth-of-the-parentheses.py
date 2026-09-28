class Solution:
    def maxDepth(self, s: str) -> int:
        op = res = 0
        
        for i in s:
            if i == "(":
                op += 1
            elif i == ")":
                op -= 1

            res = max(res, op)


        return res
        
