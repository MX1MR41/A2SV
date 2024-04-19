class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapify(stones)


        while len(stones) > 1:
            y, x = -heappop(stones), -heappop(stones)

            if y != x:
                y -= x

                heappush(stones, -y)


        return -stones.pop() if stones else 0
        
