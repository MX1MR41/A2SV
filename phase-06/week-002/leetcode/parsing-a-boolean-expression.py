class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []

        for i in expression:
            if i == "t" or i == "f":

                stack.append(True if i == "t" else False)
            elif i == "!":
                stack.append(i)
            elif i == "&":
                stack.append(i)
            elif i == "|":
                stack.append(i)
            elif i == "(":
                stack.append(i)
            elif i == ")":

                values = []
                while stack and stack[-1] != "(":
                    values.append(stack.pop())
                stack.pop()
                operator = stack.pop()

                if operator == "!":

                    stack.append(not values[0])
                elif operator == "&":

                    stack.append(all(values))
                elif operator == "|":

                    stack.append(any(values))

        return stack[0]
