class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        # modified code from https://leetcode.com/problems/maximum-subsequence-score/
        pairs = sorted(list(zip(efficiency, speed)), reverse=True)
        heap = []

        res = _sum = 0

        for n2, n1 in pairs:
            _sum += n1
            heappush(heap, n1)

            if len(heap) > k: 
                smallest = heappop(heap)
                _sum -= smallest

            res = max(res, _sum * n2)



        return res % (10**9 + 7)

