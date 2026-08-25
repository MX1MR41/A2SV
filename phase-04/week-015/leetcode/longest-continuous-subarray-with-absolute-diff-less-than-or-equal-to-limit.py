class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minDeque = deque()
        maxDeque = deque()
        start = 0
        max_length = 0

        for end in range(len(nums)):

            while minDeque and nums[minDeque[-1]] > nums[end]:
                minDeque.pop()
            minDeque.append(end)

            while maxDeque and nums[maxDeque[-1]] < nums[end]:
                maxDeque.pop()
            maxDeque.append(end)

            while nums[maxDeque[0]] - nums[minDeque[0]] > limit:
                start += 1
                if minDeque[0] < start:
                    minDeque.popleft()
                if maxDeque[0] < start:
                    maxDeque.popleft()

            max_length = max(max_length, end - start + 1)

        return max_length
