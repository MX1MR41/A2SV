class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # solution works by coupling the use of heap with a greedy approach
        # prioritize the use of bricks over ladders everyime, and in case we over-exhaust
        # our available bricks, there might have been a building where we could have used 
        # a ladder instead of the bricks we used back then, and we could use those bricks NOW.
        # The heap stores the height differences in a max-heap fashion and gives us the greatest
        # one from the past hence maximizing our use of a ladder.
        heap = []

        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff <= 0:
                continue

            bricks -= diff
            heapq.heappush(heap, -diff)

            if bricks < 0:
                if ladders == 0:
                    return i

                ladders -= 1
                bricks += -heapq.heappop(heap)
            
        return len(heights) - 1
