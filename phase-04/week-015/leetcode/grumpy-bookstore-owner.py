class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        tot = 0
        for i in range(len(grumpy)):
            if not grumpy[i]:
                tot += customers[i]
        
        _max = 0
        wind = 0
        for i in range(minutes):
            if grumpy[i]:
                wind += customers[i]
                
        _max = wind
        
        for r in range(minutes, len(customers)):
            l = r-minutes
            if grumpy[r]:
                wind += customers[r]
            if grumpy[l]:
                wind -= customers[l]
                
            _max = max(wind, _max)
            
        return tot + _max
                
        
            
