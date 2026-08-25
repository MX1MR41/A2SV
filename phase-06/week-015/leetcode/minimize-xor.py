class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:

        # if the number of set bits is equal, we just need to xor num1 with itself to get 0
        if num1.bit_count() == num2.bit_count():
            return num1


        # if num1 has more set bits, we need a number who has set bits at the most significant
        # bits of num1, and the rest zeros
        elif num1.bit_count() > num2.bit_count():
            ones = num2.bit_count()
            num1 = list(str(bin(num1))[2:])

            for i in range(len(num1)):
                if num1[i] == "1":
                    if ones:
                        ones -= 1
                    else:
                        num1[i] = "0"

            return int("".join(num1), 2)


        # if num2 has more set bits, we need a number which has the same set bits as num1
        # in addition to set bits at the least significant zero bits of num1, to keep it small
        # if any set bits remain, we add them at the front
        else:
            ones = num2.bit_count() - num1.bit_count()
            num1 = list(str(bin(num1))[2:])

            for i in range(len(num1) - 1, -1, -1):
                if num1[i] == "0" and ones:
                    num1[i] = "1"
                    ones -= 1

            if ones:
                num1 = ["1"] * ones + num1

            return int("".join(num1), 2)
