class MedianFinder:
    # we use two heaps, one max and one min. At each addition of a new num, 
    # we try to maintain the difference between them no greater than 1. This
    # ensures that our data stream is perfectly split into two

    def __init__(self):
        self.max = [] 
        self.min = []  

    def addNum(self, num: int) -> None:

        heappush(self.max, -num)  
        heappush(self.min, -heappop(self.max))

        # this one ensure that self.min doesnt house more than 1 element more than self.max
        if len(self.min) > len(self.max):
            heappush(self.max, -heappop(self.min))


    def findMedian(self) -> float:
        if len(self.max) == len(self.min):
            return (-self.max[0] + self.min[0]) / 2.0
        elif len(self.max) > len(self.min):
            return -self.max[0]
        else:
            return self.min[0]

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
