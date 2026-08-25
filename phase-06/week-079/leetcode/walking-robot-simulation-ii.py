class Robot:
    # robot just moves in a rectangle accross the borders
    # so just put those borders into one straight line 
    # and simulate movement by jumping index on that straight line

    def __init__(self, width: int, height: int):
        x = y = 0

        self.arr = []
        
        for x in range(0, width):
            self.arr.append((x, y, "East"))

        x = width - 1
        y = 1

        for y in range(1, height):
            self.arr.append((x, y, "North"))

        x = width - 2
        y = height - 1

        for x in range(width - 2, -1, -1):
            self.arr.append((x, y, "West"))

        x = 0
        y = height - 2

        for y in range(height - 2, 0, -1):
            self.arr.append((x, y, "South"))

        self.n = len(self.arr)

        self.pos = 0

        
        self.arr[0] = (0, 0, "South")
        self.moved = False

        
    def step(self, num: int) -> None:
        self.pos = (self.pos + num) % self.n

        if num > 0:
            self.moved = True
        
        
    def getPos(self) -> List[int]:
        return [self.arr[self.pos][0], self.arr[self.pos][1]]
        

    def getDir(self) -> str:
        return self.arr[self.pos][2] if self.moved else "East"

        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
