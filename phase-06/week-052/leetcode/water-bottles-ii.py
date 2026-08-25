class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        total = 0
        empty = 0
        while numBottles:
            total += numBottles
            empty += numBottles
            numBottles = 0

            if numExchange <= empty:
                empty -= numExchange
                numBottles += 1
                numExchange += 1
            else:

                break

            

        return total + numBottles
