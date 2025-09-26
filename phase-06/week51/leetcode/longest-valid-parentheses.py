class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # stack
        # keep track of opening parentheses along with the lengths of valid parentheses pairs
        # seen so far. The top of the stack will always contain the length of the last 
        # valid parentheses substring seen so far.
        # when a closing parenthesis appears, pop the length of the last valid parentheses
        # then check to see if there is an opening one to match with it, if so add 2 to the
        # previous length because the new pair is part of the valid substring
        res = 0
        stk = []

        for i in s:
            
            # append it along with 0 onto the stack cuz there is no valid substring yet
            if i == "(":
                stk.append(i)
                stk.append(0)
                continue

            # i.e. there is no matching opening parenthesis for the closing one we just got
            # the stack might be empty or it might just contain the length of the last valid
            if len(stk) < 2:
                stk.clear()
                continue

            # pop out the last length the and matching opening parenthesis
            prev_len = stk.pop()
            stk.pop()
            
            # the new pair's contribution
            prev_len += 2

            # there might be a previous valid substring immediately before the one we just
            # found with the new pair, in which case we can add up its length too
            # there will always be at max one such occurence because we keep adding them up
            # iteratively as we go and there won't be any two adjacent numbers together
            if stk and stk[-1] != "(":
                prev_len += stk.pop()

            # append the newly formed valid substring length
            stk.append(prev_len)


            res = max(res, prev_len)

        return res
