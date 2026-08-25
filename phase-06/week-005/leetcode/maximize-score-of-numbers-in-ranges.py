class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        # binary search to max-min / min-max
        
        arr = [(i, i + d) for i in sorted(start)]

        def check(x):

            nxt = arr[0][0] + x
            for s, e in arr[1:]:

                if nxt > e:
                    return False

                if nxt <= s:
                    nxt = s

                nxt += x

            return True

        l, r = 0, 2**31
        ans = 0
        while l <= r:
            mid = (l + r) // 2

            if check(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return ans
