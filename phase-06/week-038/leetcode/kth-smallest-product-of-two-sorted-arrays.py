class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # binary search
        # perform a binary search over all possible numbers as products \
        # and try to find the smallest number that which has exactly k - 1 products
        # less than it.
        # To count the number of products less than a num X, iterate over the elements
        # of nums1 and for each Y try to find a complement number Z in nums2 
        # whom if multiplied with Y would give the target X. 
        # This can be done again using binary search
        n = len(nums1)
        m = len(nums2)

        
        
        def count_less(x):
            count = 0
            
            for num in nums1:
                if num > 0:
                    # count all the numbers less than and equal to x / num
                    count += bisect_right(nums2, x / num) 
                elif num < 0:
                    # count all numbers greater than or equal to x / num
                    count += m - bisect_left(nums2, x / num)
                else: 
                    # multiplying 0 with any of the nums2 would give 0 which is <= x if x >= 0
                    if x >= 0:
                        count += m

            return count

        
        l, r = -10**10, 10**10
        res = r

        while l <= r:
            mid = (l + r) // 2
            if count_less(mid) >= k:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res
