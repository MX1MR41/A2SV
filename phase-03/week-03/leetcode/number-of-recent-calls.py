class RecentCounter:

    def __init__(self):
        self.requests = deque()
        self.arr = []


        

    def ping(self, t: int) -> int:
        self.requests.append(t)
        self.arr.append(t)
        n = len(self.requests)
        diff = t - 3000
        for i in self.arr:
            if i < diff:
                self.requests.popleft()

        self.arr = list(self.requests)
        return len(self.requests)

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)