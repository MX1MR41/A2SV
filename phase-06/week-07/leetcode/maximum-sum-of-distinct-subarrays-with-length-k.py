class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # sliding window
        # apparently checking len(dictionary) is O(1) 
        window = sum(nums[:k])
        count = Counter(nums[:k])

        maximum_sum = window if len(count) == k else 0

        for r in range(k, len(nums)):
            window += nums[r]
            count[nums[r]] += 1

            window -= nums[r - k]
            count[nums[r - k]] -= 1
            if count[nums[r - k]] == 0:
                del count[nums[r - k]]

            if len(count) == k:
                maximum_sum = max(window, maximum_sum)

        return maximum_sum
