class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        one = {
            1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
            6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
        }

        ten = {
            2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty",
            6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"
        }

        teen = {
            10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen",
            16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"
        }

        def two_digits(num):
            if num == 0:
                return ""
            elif num < 10:
                return one[num]
            elif num < 20:
                return teen[num]
            else:
                tens_place = num // 10
                ones_place = num % 10
                return ten[tens_place] + (" " + one[ones_place] if ones_place > 0 else "")

        def three_digits(num):
            hundreds_place = num // 100
            rest = num % 100
            if hundreds_place and rest:
                return one[hundreds_place] + " Hundred " + two_digits(rest)
            elif not hundreds_place and rest:
                return two_digits(rest)
            elif hundreds_place and not rest:
                return one[hundreds_place] + " Hundred"
            else:
                return ""

        units = ["", "Thousand", "Million", "Billion"]
        res = ""
        unit_index = 0

        while num > 0:
            if num % 1000 != 0:
                res = three_digits(num % 1000) + ((" " + units[unit_index]) if units[unit_index] else "") + " " + res
            num //= 1000
            unit_index += 1

        return res.strip()
