class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # this approach works by using a mononically decreasing stack and reverse traversal
        # we initialize a last variable that will hold the '2' number
        # our stack will hold the '3' number(s)
        # and we will traverse in reverse to find the '1' number
        # since we are using a monotonically increasing stack and changing the last variable
        # to the last num which which was less than the num(s) in our stack 
        # AND to the right of the num in stack, 
        # last will always have a value smaller than the num(s) in stack.
        # Therefore, if we ever find a num smaller than the last variable, we can be sure that
        # there is also a num(s) greater than last that come before it, hence 132 pattern
        if len(nums) < 3:
            return False
        
        stk = []
        last = float('-inf')  

        for num in reversed(nums):
            if num < last:
                return True 

            while stk and stk[-1] < num:
                last = stk.pop() 

            stk.append(num)  
        
        return False
