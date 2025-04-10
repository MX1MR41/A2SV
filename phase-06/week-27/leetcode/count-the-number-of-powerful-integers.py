class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
    
        def calculate(x: str, s: str, limit: int) -> int:
            # If x is shorter than s, no valid numbers exist
            if len(x) < len(s):
                return 0
            # If x has the same length as s, check directly if s is <= x
            if len(x) == len(s):
                return 1 if x >= s else 0

            # Extract the last len(s) characters of x (the suffix part of the bound)
            suffix = x[len(x) - len(s):]
            count = 0
            # Number of digits in x that form the prefix (excluding the suffix part)
            pre_len = len(x) - len(s)

            # Process each digit in the prefix from left to right
            for i in range(pre_len):
                # When the current digit exceeds the allowed limit,
                # all choices for this and the remaining digits are valid combinations.
                if limit < int(x[i]):
                    # (limit + 1) choices for each remaining position
                    count += (limit + 1) ** (pre_len - i)
                    return count
                
                # For this position, add counts contributed by all digits less than the current digit
                count += int(x[i]) * (limit + 1) ** (pre_len - 1 - i)

            # If the exact prefix of x (all digits processed)
            # followed by suffix s is <= x (i.e., x's suffix is >= s),
            # count one additional valid number.
            if suffix >= s:
                count += 1

            return count

        # Convert the bounds to strings for digit-by-digit comparison.
        # We subtract 1 from start to count numbers strictly less than start.
        start_str = str(start - 1)
        finish_str = str(finish)

        # The powerful count in range [start, finish] is count(finish) - count(start - 1)
        return calculate(finish_str, s, limit) - calculate(start_str, s, limit)
