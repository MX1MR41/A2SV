class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # we count the number of times each bit is 1 and if total % 3 == 1
        # then that bit is 1 in the number that appears one time only 
        cnt = [0] * 32

        for num in nums:
            # for negative numbers, we add 2**32 to them to wrap them around
            # and the new value would be between [2**32 - 1, 2**31] inclusive
            # which is the two's complement representation of negative numbers
            # (negating all bits then adding 1)
            if num < 0:
                num += 2 ** 32

            for i in range(32):
                if num & (1 << i):
                    cnt[i] += 1

        ans = 0
        for ind, freq in enumerate(cnt):
            if freq % 3:
                ans |= 1 << ind

        if ans >= 2 ** 31:
            ans -= 2 ** 32

        return ans
