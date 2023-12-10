class Solution:
    def largestOddNumber(self, num: str) -> str:

        sys.set_int_max_str_digits(int(10e5))

        if int(num) % 2:
            return num


        for i in reversed(range(len(num))):
            if int(num[i]) % 2:
                return num[:i+1]

        return ""
            
