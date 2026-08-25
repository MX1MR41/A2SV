class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        res = 0

        # the greedy approach would be to exhaust our allowed doubling operations
        # from the target down to 1. So instead of doubling, we do halving
        while maxDoubles and target > 1:
            if target % 2:
                # if the number is odd, we subtract 1 to make it even for halving
                target -= 1
            else:
                # if even, then we just halve
                target //= 2
                maxDoubles -= 1

            res += 1 # count every operation

        # if the number still isnt 1, we add its difference from 1 to our result
        # since we have exhausted our halving operation and can now only do increments +1
        return res + target - 1 if target > 1 else res

        