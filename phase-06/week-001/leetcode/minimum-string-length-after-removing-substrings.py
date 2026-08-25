class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for i in s:
            if i == "B":
                if stack and stack[-1] == "A":
                    stack.pop()
                else:
                    stack.append(i)

            elif i == "D":
                if stack and stack[-1] == "C":
                    stack.pop()
                else:
                    stack.append(i)

            else:
                stack.append(i)

        return len(stack)

        
