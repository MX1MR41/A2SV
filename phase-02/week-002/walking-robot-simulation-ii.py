class Robot:
    def __init__(self, width: int, height: int):
        self.D="East"
        self.pos=[0,0]
        self.arr=[width-1,height-1]
        self.width, self.height = width, height
        
    def step(self, num: int) -> None:
        tot =((self.height+self.width-2)*2)
        num = num % tot 
        if num != 0:
           i=0
           while i < num:
                if self.D=="East":
                    if self.pos[0]==self.width-1:
                        num += 1
                        self.D="North"
                    else:
                        self.pos[0]+=1

                elif self.D=="West":
                    if self.pos[0]==0:
                        num += 1
                        self.D="South"
                    else:
                        self.pos[0]-=1
                elif self.D=="North":
                    if self.pos[1]==self.height-1:
                        num += 1
                        self.D = "West"
                    else:
                        self.pos[1] += 1
                elif self.D == "South":
                    if self.pos[1] == 0:
                        num += 1
                        self.D = "East"
                    else:
                        self.pos[1] -= 1
                i += 1      
        elif self.pos == [0,0] and self.D == "East":
            self.D = "South"
      
    def getPos(self) -> List[int]:
        return self.pos

    def getDir(self) -> str:
        return self.D

