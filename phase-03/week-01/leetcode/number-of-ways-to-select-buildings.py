class Solution:
    def numberOfWays(self, s: str) -> int:
        cnt = Counter(s)
        # the total number of zeros and ones that we'll use as suffix sums
        suff_zeros, suff_ones = cnt['0'], cnt['1'] 
        # variables to store the counts of 0's and 1's seen so far, as prefix sum
        pref_zeros, pref_ones = 0, 0 
        res = 0

        for building in s:
            if building == "0":
                # total combinations with this building in the middle is equal to
                # number of ones before it times number of ones after it
                res += pref_ones * (suff_ones - pref_ones)
                pref_zeros += 1
            else:
                res += pref_zeros * (suff_zeros - pref_zeros)
                pref_ones += 1


        return res


        

        