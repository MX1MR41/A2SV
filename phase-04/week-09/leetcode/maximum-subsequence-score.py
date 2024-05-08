class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # greedy algorithm using heap
        # the greedy part is calculating for each number in nums2
        # the maximum possible sum that will be multiplied
        # the summation numbers will be stored in a heap of size k
        # heap cuz we will need to know the smallest num to remove from our sum to affect it least
        pairs = sorted(list(zip(nums2, nums1)), reverse=True)
        heap = []

        res = _sum = 0

        for n2, n1 in pairs:
            _sum += n1
            heappush(heap, n1)

            if len(heap) > k: # we need to un-choose one element, greediest choice is the smallest
                smallest = heappop(heap)
                _sum -= smallest

            if len(heap) == k: # one valid combination
                res = max(res, _sum * n2)



        return res
