class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        # two pointers
        
        res = 0

        m = len(nums1)
        n = len(nums2)

        i = j = 0

        while i < m and j < n:
            while j < i:
                j += 1

            if j >= n:
                break

            if nums1[i] <= nums2[j]:
                res = max(res, j - i)

                j += 1

            else:
                i += 1

        return res
        
