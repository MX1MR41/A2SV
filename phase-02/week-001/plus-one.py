class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        if digits[-1] < 9: # only the last digit needs to be added
            digits[-1] += 1
            return digits
        else:
            n = set(digits)
            if len(n) == 1 and 9 in n: # the whole list is just a bunch of 9s
                ans = [0] * (len(digits) + 1)
                ans[0] = 1
                return ans
            else:  #all other cases
                i = len(digits) - 1

                while i >= 0: #find the first non-9 digit from the last
                    i -= 1
                    if digits[i] != 9:
                        break


                digits[i] += 1
                i += 1

                while i < len(digits): # make all the digits 0
                    digits[i] = 0
                    i += 1

                return digits
