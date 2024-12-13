class Solution:
    def findScore(self, nums: List[int]) -> int:
        heap = [(num, ind) for ind, num in enumerate(nums)]
        heapify(heap)

        score = 0
        marked = set()

        while heap:
            while heap and heap[0][1] in marked:
                heappop(heap)

            if heap:
                num, ind = heappop(heap)
                marked.add(ind)
                marked.add(ind - 1)
                marked.add(ind + 1)
                score += num


        return score
