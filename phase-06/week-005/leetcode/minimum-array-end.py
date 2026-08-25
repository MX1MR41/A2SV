class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # start from x, then you need to find the (n-1)th number greater than x
        # that also has the same bits set as x
        # convert x into binary representation, then try to fill out the zeros
        # by (n-1). Essentially try to fit it in without touching the set bits of x
        bits = [0] * 64

        for i in range(64):
            if x & (1 << i):
                bits[i] = 1

        add = n - 1
        add_bits = [0] * 32

        for i in range(32):
            if add & (1 << i):
                add_bits[i] = 1

        ind = 0
        for i in range(32):
            while ind < 64 and bits[ind] == 1:
                ind += 1

            if ind < 64:
                bits[ind] = add_bits[i]
            ind += 1

        ans = 0

        for i in range(64):
            if bits[i]:
                ans |= 1 << i

        return ans
