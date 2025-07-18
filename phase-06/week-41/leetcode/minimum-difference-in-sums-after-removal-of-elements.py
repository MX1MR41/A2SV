class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        # heap + dp
        # go over every index and consider it as a split point
        # for an index to be a split point we need to find the minimum sum up to that index
        # that could be formed from n numbers and the maximum sum after that index.
        # so we precompute these sums using a heap of size n from both sides

        n = len(nums)
        m = n//3

        dp_left = [float("inf")] * n

        heap = []
        heap_sum = 0

        for i in range(n):
            num = nums[i]

            heappush(heap, -num)
            heap_sum += -num

            if len(heap) > m:
                heap_sum -= heappop(heap)

            if len(heap) == m:
                dp_left[i] = -heap_sum


        dp_right = [float("-inf")] * n
        heap = []
        heap_sum = 0

        for i in range(n - 1, -1, -1):
            num = nums[i]

            heappush(heap, num)
            heap_sum += num

            if len(heap) > m:
                heap_sum -= heappop(heap)

            if len(heap) == m:
                dp_right[i] = heap_sum


        res = float("inf")


        for i in range(n - 1):
            res = min(res, dp_left[i] - dp_right[i + 1])

        return res



        

