class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1  # Ensure nums1 is the smaller array
        
        n, m = len(nums1), len(nums2)
        total = n + m
        half = total // 2

        l, r = 0, n - 1

        while True:
            i = (l + r) // 2  # Midpoint for nums1
            j = half - (i + 1) - 1  # Corresponding index in nums2

            # Handle edge cases for partition boundaries
            nums1_left = nums1[i] if i >= 0 else float("-inf")
            nums1_right = nums1[i + 1] if i + 1 < n else float("inf")
            nums2_left = nums2[j] if j >= 0 else float("-inf")
            nums2_right = nums2[j + 1] if j + 1 < m else float("inf")

            # Check if we have a valid partition
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if total % 2 == 0:
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
                else:
                    return min(nums1_right, nums2_right)

            # Adjust search range
            elif nums1_left > nums2_right:
                r = i - 1  # Move left in nums1
            else:
                l = i + 1  # Move right in nums1
