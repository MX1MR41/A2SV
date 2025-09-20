# queue + binary search
# keep track of the packets in a queue and also for every destination keep track of
# its packets in a separate queue
# when adding a packet, check size then add the packet to the global queue and the queue
# specific to the destination as well
# when removing a packet, remove from the front of the global queue and from the front of
# the respective destination queue as well
# to get count, find the start and end indices using binary search, return end - start + 1

class Router:

    def __init__(self, memoryLimit: int):
        self.capacity = memoryLimit
        self.queues = defaultdict(deque)
        self.queue = deque()
        self.size = 0
        self.seen = set()        

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        newPack = (source, destination, timestamp)
        if newPack in self.seen:
            return False

        if self.size == self.capacity:
            self.forwardPacket()

        self.queue.append(newPack)
        self.queues[newPack[1]].append(newPack)
        self.seen.add(newPack)
        self.size += 1

        return True
        

    def forwardPacket(self) -> List[int]:
        if self.size == 0:
            return []

        oldPack = self.queue.popleft()
        self.queues[oldPack[1]].popleft()
        self.seen.discard(oldPack)
        self.size -= 1

        return list(oldPack)
        

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        queue = self.queues[destination]
        if not queue or queue[0][2] > endTime or queue[-1][2] < startTime:
            return 0

        l = 0
        r = len(queue) - 1
        start = r
        while l <= r:
            mid = (l + r)//2
            if queue[mid][2] >= startTime:
                start = mid
                r = mid - 1
            else:
                l = mid + 1

        l = 0
        r = len(queue) - 1
        end = 0
        while l <= r:
            mid = (l + r)//2
            if queue[mid][2] <= endTime:
                end = mid
                l = mid + 1
            else:
                r = mid - 1

        if start > end:
            return 0

        return end - start + 1

        
        


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
