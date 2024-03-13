# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        res = l

        while l <= r:
            mid = (l + r)//2
            g = guess(mid)

            if not g:
                return mid
            elif g == 1:
                l = mid + 1
                res = mid
            else:
                r = mid - 1
                # res = mid

        return res

        