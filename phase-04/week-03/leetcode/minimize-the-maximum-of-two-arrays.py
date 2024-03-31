class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        # binary search coupled with arithmetics
        LCM = divisor1 * divisor2 // gcd(divisor1, divisor2)

        def check(x):
            # count of numbers not divisible by a divisor d upto x
            # is calculated as such because there are x//d groups each with one
            # number divisible by d. And the modulo part accounts for incomplete
            # groups that occur in case the x isn't perfectly divisble into groups with d nums each
            cnt1 = x // divisor1 * (divisor1 - 1) + x % divisor1
            cnt2 = x // divisor2 * (divisor2 - 1) + x % divisor2
            total = x // LCM * (LCM - 1) + x % LCM
            return (
                cnt1 >= uniqueCnt1 and
                cnt2 >= uniqueCnt2 and
                total >= uniqueCnt1 + uniqueCnt2
            )

        res = bisect_left(range(10**10), True, key=check)
      
        return res