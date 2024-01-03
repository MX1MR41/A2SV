class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        ans = float("inf")
        n1, n2 = len(nums1), len(nums2)
        i , j = 0, 0

        while i < n1 and j < n2:
            a, b = nums1[i], nums2[j] 

            if a == b:
                ans = min(ans, a)
                j += 1
                i += 1

            elif a < b:
                i += 1

            elif a > b:
                j += 1

        if ans == float("inf"):
            return -1
        else: 
            return ans
        