class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # we do a binary search over the set of possible outputs
        # which range from the maximum weight to the sum of all weights
        # cuz the maximum weight is the minimum required capacity to carry 
        # all weights even if they're one by one.
        # and the sum is the limit because with that capacity we can take all at once
        first, last = max(weights), sum(weights)
        tot = last
        res = float("inf")

        while first <= last:
            mid = (first + last)//2

            # for each capacity "mid", we calculate the days it takes
            curr_days = 1
            n = len(weights)
            temp = 0
            
            for r in range(n):
                if temp + weights[r] > mid:
                    curr_days += 1
                    temp = 0

                temp += weights[r]
                

            # a valid capacity
            if curr_days <= days:
                res = min(res, mid)
                # we exhaustively search to the left to find 
                # an even smaller valid capacity
                last = mid - 1
            else:
                first = mid + 1

        return res

                





        
        