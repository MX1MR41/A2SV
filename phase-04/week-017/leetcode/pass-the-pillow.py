class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        flag = True
        curr = 1
        while time:
            if curr ==1:
                curr += 1
                flag = True
            elif curr == n:
                curr -= 1
                flag = False
            else:
                if flag:
                    curr += 1
                else:
                    curr -= 1
                    
            time -= 1
        return curr
