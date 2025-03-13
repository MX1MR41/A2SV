class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        leftBound = -1  # Last index where nums[i] is out of range
        lastMin = -1  # Last index where nums[i] == minK
        lastMax = -1  # Last index where nums[i] == maxK
        count = 0

        for r in range(len(nums)):
            if nums[r] < minK or nums[r] > maxK:
                leftBound = r  # Reset the valid window
            if nums[r] == minK:
                lastMin = r  # Update last position of minK
            if nums[r] == maxK:
                lastMax = r  # Update last position of maxK

            # Valid subarray count contribution
            count += max(0, min(lastMin, lastMax) - leftBound)

        return count
