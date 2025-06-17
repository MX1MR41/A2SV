class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        # math
        # let n = 4, m = 4 without considering k for a moment, 
        # i.e, all adjacent nums are different.
        # We could have 4*3*3*3 arrays i.e. we can choose from 4 numbers [1, 4] 
        # for the 1st position, 3 for the second, etc...
        # Now let's say we wanted k = 1 i.e. we want two adjacent elements to be same
        # so we have the following options 4*3*3*1, 4*3*1*3, 4*1*3*3,
        # we need to compute number of ways we can position that 1 from 3 positions
        # i.e 3 choose 1 => combinations(3, 1).
        # total = 4*3*3*1 + 4*3*1*3 + 4*1*3*3 = 3 * (4*3*3*1) = comb(3,1) * (4*3*3*1)
        # total = num ways to choose numbers * num ways to spread the k nums


        MOD = pow(10, 9) + 7

        count = (m * pow(m - 1, n - 1 - k, MOD)) % MOD

        count = (count * comb(n - 1, k)) % MOD

        return count 
