class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # dp
        # while traversing, we keep track of three variables
        # 1) largest sum with modulo equal to 0
        # 2) largest sum with modulo equal to 1
        # 3) largest sum with modulo equal to 2
        # and update them based on what the current num + those three variables would give
        # e.g. a modulo 1 plus a modulo 2 would give a modulo 3,
        # a modulo 2 plus a modulo 2 would give a modulo 1 etc...
        # but update the variables iff their operands are not zero, otherwise wrong answer

        zero = one = two = 0
        for num in nums:

            nzero = zero
            none = one
            ntwo = two

            if num % 3 == 0:
                nzero = zero + num

                if one:
                    none = one + num

                if two:
                    ntwo = two + num

            elif num % 3 == 1:

                if two:
                    nzero = max(zero, two + num)

                if zero:
                    none = max(one, zero + num)

                if one:
                    ntwo = max(two, one + num)

                none = max(none, num)

            else:
                if one:
                    nzero = max(zero, one + num)

                if two:
                    none = max(one, two + num)

                if zero:
                    ntwo = max(two, zero + num)

                ntwo = max(ntwo, num)

            zero = nzero
            one = none
            two = ntwo

        return zero
