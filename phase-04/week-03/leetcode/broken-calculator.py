class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        res = 0
        while startValue < target:
            if not target % 2:
                target //= 2
            else:
                target += 1
            
            res += 1
            
        # this handles cases when the target has gone below the startValue
        return res + startValue - target