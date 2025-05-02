class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # sliding window + monotonic queues
        # we sweep a right pointer through nums, keeping a window [start..right]
        # that only contains values between minK and maxK (inclusive).
        # minque stores indices of potential minima in increasing order of value.
        # maxque stores indices of potential maxima in decreasing order of value.
        
        count = 0
        start = 0  # left boundary of the current valid window
        minque, maxque = deque(), deque()

        for right, rnum in enumerate(nums):
            # if current value is out of [minK..maxK], no subarray crossing it is valid
            if rnum < minK or rnum > maxK:
                minque.clear()
                maxque.clear()
                start = right + 1  # reset window to begin after this bad index
                continue

            
            while minque and nums[minque[-1]] >= rnum:
                minque.pop()
            minque.append(right)

            
            while maxque and nums[maxque[-1]] <= rnum:
                maxque.pop()
            maxque.append(right)

            # valid window
            if nums[minque[0]] == minK and nums[maxque[0]] == maxK:
                # the first position where both minK and maxK appear
                left = min(minque[0], maxque[0])
                # any subarray starting at start..left and ending at right is valid
                count += (left - start + 1)

        return count
