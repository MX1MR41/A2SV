class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = []

        for ind, num in enumerate(nums):
            if len(heap) < k:
                heappush(heap, (num, ind))
                continue

            if num > heap[0][0]:
                heappop(heap)
                heappush(heap, (num, ind))

        
        res = sorted(heap, key = lambda x: x[1])
        return [x[0] for x in res]
