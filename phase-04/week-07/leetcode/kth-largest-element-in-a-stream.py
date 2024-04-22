class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for n in nums:
            self.add(n)
        
    def add(self, val: int) -> int:
        heappush(self.heap, val)
        # maintian a heap of only size k because it might get very big
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]
        


