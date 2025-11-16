class Solution:
    def numSub(self, s: str) -> int:
        # counting
        # keep track of the number of consecutive ones seen so far
        # and when that consecutive block ends, count the number of subarrays by arithmetic formula
        total = 0
        ones = 0

        for i in s:
            if i == "1":
                ones += 1
            else:
                total += (ones) * (ones + 1) // 2
                ones = 0

        if ones > 0:
            total += (ones) * (ones + 1) // 2

        return total % (10**9 + 7)
        
