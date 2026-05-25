class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # prefix sum, difference array, line sweep
        n = len(s)
        
        can = [0] * n
        can[0] = 1
        can[1] = -1

        for i in range(n):
            
            if i > 0:
                can[i] += can[i - 1]
            if can[i] <= 0 or s[i] != "0":
                continue


            start = i + minJump

            if start < n:
                can[start] += 1

            end = i + maxJump + 1
            if end < n:
                can[end] -= 1

        return s[-1] == "0" and can[-1] > 0




        
