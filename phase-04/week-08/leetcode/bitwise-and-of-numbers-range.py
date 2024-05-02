class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # when AND-ing all numbers in a given range, the answer will have bit 0
        # at position i and all positions to the right of i if there exists some position j
        # to the left of position i where left and right have different bit values.
        # If j-th bit is different for left and right, then there must have been a num 
        # left < num < right which had an i-th bit (i to the right of j) that was 0
        n = max(right.bit_length(), left.bit_length())

        mask = 0
        res = 0
        for i in reversed(range(n)):
            mask = mask | 1 << i

            x, y = mask & left, mask & right

            if x != 0 and x == y:
                res = mask & x
            else:
                return res

        return res
