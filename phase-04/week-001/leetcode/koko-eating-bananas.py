class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # in this implementation of binary search, we search through 
        # the set of answers instead of the set of inputs
        res = m = max(piles)

        l, r = 1, m

        while l <= r:

            mid = (l+r)//2

            curr_hours = 0 

            for i in piles:
                curr_hours += ceil(i/mid)

            if curr_hours <= h:
                res = min(res, mid)
                r = mid - 1

            else:
                l = mid + 1

        return res

        