class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        # binary search onside binary search

        def check(t): # check if this time is enought to level the mountain
            total = 0

            for w in workerTimes:
                
                # find maximum amount of mountain this worker can obliterate
                l, r = 1, mountainHeight
                deduct = 0
                while l <= r:
                    mid = (l + r)//2
                    d_t = w * (mid * (mid + 1)//2)
                    if d_t <= t:
                        deduct = mid
                        l = mid + 1
                    else:
                        r = mid - 1

                total += deduct

            return total >= mountainHeight




        max_w = max(workerTimes)
        max_time = (mountainHeight * (mountainHeight + 1)//2) * max_w
        

        # find the minimum time
        l, r = 0, max_time
        res = r
        while l <= r:
            mid = (l + r)//2
            if check(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res


        
