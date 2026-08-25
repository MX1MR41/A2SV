class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # constraints denote that k <= len(nums) indicating that the max element
        # is the upper bound since using it as the divisor would make all elems 1
        # hence a the sum would be equal to the length
        l, r = 1, max(nums)

        ans = r 

        while l <= r:
            mid = (l+r)//2

            curr = 0

            for i in nums:
                curr += ceil(i/mid)

            # meaning our divsor is too small
            if curr > threshold:
                l = mid + 1
            else: # we found the latest valid answer, keep searching lower
                ans = mid
                r = mid - 1

        return ans
        