class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {}

        while True:
            if n in seen:
                return False
            else:
                sum = 0
                s = str(n)
                for i in s:
                    sum += int(i)**2
                seen[n] = sum
                n = sum
                if sum == 1:
                    return True

                
                

        