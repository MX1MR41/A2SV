class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # heap + prefix sum
        # store (prefix_sum, index) in heap
        # for every prefix_sum, try to find a previous prefix sum whom if deducted from the 
        # current prefix sum would yield a valid subarray

        heap = []
        n = len(nums)
        prefix_sum = 0
        res = float("inf")

        for i in range(n):
            
            prefix_sum += nums[i]
            if prefix_sum >= k:
                res = min(res, i + 1)

            while heap and prefix_sum - heap[0][0] >= k:
                last_prefix_sum, last_index = heappop(heap)
                res = min(res, i - last_index)

            heappush(heap, (prefix_sum, i))


        return res if res != float("inf") else - 1
