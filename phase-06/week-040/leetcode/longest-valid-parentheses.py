class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        stk = []

        for i in s:

            if i == "(":
                stk.append(i)
                stk.append(0)
                continue

            if not stk:
                continue

            prev = stk.pop()
            
            if stk and stk[-1] == "(":
                stk.pop()
            else:
                stk.clear()
                continue

            prev += 2

            while stk and stk[-1] != "(":
                prev += stk.pop()

            stk.append(prev)

            res = max(res, prev)

        return res
