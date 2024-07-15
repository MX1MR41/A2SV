class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        tot = numBottles 
        while numBottles >= numExchange: 
            tot += numBottles//numExchange 
            numBottles += -( numBottles//numExchange)*numExchange + numBottles//numExchange 
            
        return tot
            
        
