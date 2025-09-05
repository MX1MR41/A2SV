class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        # bit manipulation
        # for step S, we deduct - sum_of_powers_of_two - S(num2) from num1
        # i.e. we want num1 - sum_of_powers_of_two - S(num2) = 0 
        # sum_of_powers_of_two = num1 - S(num2)
        # if we can find S powers of two such that they sum up to sum_of_powers_of_two,
        # then we can make um1 reach zero at step S
        # a quick trick would be to count the number of 1 bits in sum_of_powers_of_two
        # and if they happen to be equal to S, it is valid because we can treat those
        # bits as separate powers of two summed up 
        # i.e. if i'th bit == 1, 2**i is in the sum
        # another case is if sum_of_powers_of_two == steps then we can separate it into
        # S 2^0's or 1's. Last case is if sum_of_powers_of_two has less than S 1 bits
        # but is greater than the minimum required sum of powers of two, 
        # i.e. 2 consecutive 1 bits like 1111 for S = 4. in this case 10011 is valid
        # because we can decompose it as (10000) + 1 + 1 = (1000 + 1000) + 1 + 1 which
        # are exactly S powers of two


        steps = 0

        while True:
            steps += 1
            sum_of_two_pows = num1 - (steps * num2)
            if sum_of_two_pows <= 0:
                return -1

            if sum_of_two_pows.bit_count() == steps or sum_of_two_pows == steps:
                return steps

            if sum_of_two_pows.bit_count() < steps:

                minimum = 0
                for i in range(steps):
                    minimum |= 1 << i

                if sum_of_two_pows >= minimum:
                    return steps

        return -1
