class Solution:
    def trap(self, height: List[int]) -> int:
        # we use a monotonically decreasing stack
        # each time we get a height that is greater than the last seen one(s)
        # we keep popping from our stack and computing the water level trapped so far
        n = len(height)

        if n == 0:
            return 0
        
        res = 0
        stk = []
        
        for i in range(n):

            while stk and height[i] > height[stk[-1]]:
                top = stk.pop()
                if not stk:
                    break
                length = i - stk[-1] - 1
                level = min(height[i], height[stk[-1]]) - height[top]
                print(height[i], height[top], length, level)
                res += length * level
            
            stk.append(i)
        
        return res