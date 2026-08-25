class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        # binary search
        # there is a sorted property which is the total trips that could be taken 
        # over a sorted time units
        
        def total(t):
            tot = 0
            for bus in time:
                tot += t//bus

            return tot

        l, r = 0, 2**50
        ans = r
        while l <= r:
            mid = (l + r)//2
            if total(mid) >= totalTrips:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans
        minimum-time-to-complete-trips.py
