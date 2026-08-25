class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-gift for gift in gifts]
        heapify(heap)

        for _ in range(k):

            if heap:
                largest = -heappop(heap)
                left = int(largest ** (0.5))
                if left:
                    heappush(heap, -left)

        return sum(-gift for gift in heap)
