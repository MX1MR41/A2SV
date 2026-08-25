class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        # stack
        # use a stack to simulate the process of matchmaking
        # greedily match the earliest possible occurence match

        def cycle(letter):
            nxt = ord(letter) + 1
            if nxt > 122:
                nxt = 96 + (nxt % 122)
            return chr(nxt)
            

        s1, s2 = list(str1), list(str2)
        stack = s2[::-1]
        


        for i in s1:
            if stack and (stack[-1] == cycle(i) or stack[-1] == i):
                stack.pop()

        return not stack
        
