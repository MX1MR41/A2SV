class Solution:
    def checkPowersOfThree(self, n: int) -> bool:

        while n >= 1:
            if not n % 3:
                n /= 3

            elif n % 3 == 1:
                n //= 3

            elif n % 3 >= 1:
                return False
        
        
        return True
        