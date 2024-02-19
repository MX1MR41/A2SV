class MinStack:

    def __init__(self):
        self.stk = []
        self.min = []
        

    def push(self, val: int) -> None:
        if not self.min:
            self.min.append(val)
        else:
            if val <= self.min[-1]:
                self.min.append(val)

        self.stk.append(val)
        

    def pop(self) -> None:
        p = self.stk.pop()
        if self.min and p == self.min[-1]:
            self.min.pop()
        
        return p
        

    def top(self) -> int:
        return self.stk[-1]
        

    def getMin(self) -> int:
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()