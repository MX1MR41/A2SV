class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        heap = [(num, index) for index, num in enumerate(nums)]
        heapify(heap)
        for _ in range(k):
            num, ind = heappop(heap)
            num *= multiplier

            heappush(heap, (num, ind))

        heap.sort(key = lambda x: x[1])
        return [i[0] for i in heap]
