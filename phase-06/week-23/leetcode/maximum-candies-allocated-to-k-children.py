class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # binary search
        if sum(candies) < k:
            return 0

        def check(x):
            count = 0
            for i in candies:
                if i == x:
                    count += 1
                elif i > x:
                    count += i//x

            return count >= k


        l, r = 1, sum(candies)
        res = 0
        while l <= r:
            mid = (l + r)//2
            if check(mid):
                res = mid
                l = mid + 1
            else:
                r = mid - 1

        return res
        
