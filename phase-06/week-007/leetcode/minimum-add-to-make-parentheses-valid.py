class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # stack with two passes
        # first eliminate unmatched closing parantheses
        # then eliminate unmatched opening parantheses
        opening = 0
        stack = []
        for i in s:
            if i == ")":
                if opening > 0:
                    stack.append(i)
                    opening -= 1
            else:
                stack.append(i)
                if i == "(":
                    opening += 1

        stack.reverse()

        stack2 = []

        closing = 0
        for i in stack:
            if i == "(":
                if closing > 0:
                    stack2.append(i)
                    closing -= 1
            else:
                stack2.append(i)
                if i == ")":
                    closing += 1

        stack2.reverse()
        return "".join(stack2)
