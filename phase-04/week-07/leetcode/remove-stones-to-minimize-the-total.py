class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        tot = 0
        arr = []
        
        for i in piles:
            arr.append(-i)
            tot += i

        heapify(arr)

        for _ in range(k):
            curr = -heappop(arr)
            tot -= curr//2
            curr = curr - curr//2
            heappush(arr, -curr)

        return tot
        
