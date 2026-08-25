class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        s = int(s,2)
        while s > 1:
            if not s % 2:
                s >>= 1
            else:
                s += 1

            steps += 1

        return steps
        
