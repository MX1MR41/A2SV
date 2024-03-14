class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # the approach is to use a monotonic queue coupled with prefix sum
        # we pre-calculate the prefix sum array, and in our queue we store
        # indices based on increasing prefix sum values
        # then for each prefix sum, we keep popping from the left of the queue
        # i.e shrinking the subarray from the left as lonng as the 
        # difference between the prefix sums of the current index and the front of the
        # queue satisfy the condition. 

        # we also prune the queue from the right if the last indices of the queue
        # have prefix sums greater than or equal to our current prefix sum. 
        # this ensures that the queue will stay monotonic

        n, res = len(nums), float("inf")
        # initializing a prefix sum array
        pre = [0 for _ in range(n)]
        q = deque()
        # populating the prefix sum array
        for i in range(n):
            pre[i] = nums[i] + (pre[i - 1] if i > 0 else 0)
            # we can preprocess the result here
            if pre[i] >= k:
                res = min(res, i + 1)

        for i in range(n):
            
            # shrinking from the left and minimizing our result
            while q and pre[i] - pre[q[0]] >= k:
                res = min(res, i - q.popleft())

            # pruning from the right of queue to maintain monotonicity
            while q and pre[q[-1]] >= pre[i]:
                q.pop()

            q.append(i)

        return -1 if res == float("inf") else res
        
        