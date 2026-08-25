class MyCalendarTwo:

    def __init__(self):
        self.calendar = []
        

    def book(self, start: int, end: int) -> bool:
        temp = []
        for s, e in self.calendar:
            if start < e and end > s:
                if temp: 
                    for lasts, laste in temp:
                        if s < laste and e > lasts: return False
                temp.append((s,e))

        self.calendar.append((start, end))

        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
