class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # Stack with two passes
        # On the first pass, try to match the extra closing parentheses
        # On the second pass, try to match the extra opening parentheses
        # Keep count of both opening and closing seen so far
        # Use a stack to store the indices of respective parentheses that we can flip
        # Each time an imbalance occurs, grab the nearest index from the stack and flip it
        # Finally, check if s has become balanced

        s = list(s)  # Convert the string to a list for mutability
        n = len(s)
        stack = []  # Stack to store indices of parentheses that can be flipped

        open_count = close_count = 0

        # First pass: resolve excess closing parentheses
        for i in range(n):
            if s[i] == "(":
                open_count += 1
            else:  # s[i] == ")"
                close_count += 1
                if locked[i] == "0":
                    stack.append(i)

            # Handle imbalance: more closing than opening
            if close_count > open_count:
                if stack:
                    index_to_flip = stack.pop()
                    s[index_to_flip] = "("
                    close_count -= 1
                    open_count += 1

        stack = []
        open_count = close_count = 0

        # Second pass: resolve excess opening parentheses
        for i in range(n - 1, -1, -1):
            if s[i] == "(":
                open_count += 1
                if locked[i] == "0":
                    stack.append(i)
            else:
                close_count += 1

            # Handle imbalance: more opening than closing
            if open_count > close_count:
                if stack:
                    index_to_flip = stack.pop()
                    s[index_to_flip] = ")"
                    open_count -= 1
                    close_count += 1


        # Final check: validate the balanced string
        stack = []
        for char in s:
            if char == "(":
                stack.append(char)
            else: 
                if not stack:
                    return False
                stack.pop()

        return not stack
