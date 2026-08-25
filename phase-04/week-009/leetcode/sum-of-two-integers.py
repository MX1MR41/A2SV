class Solution:
    def getSum(self, a: int, b: int) -> int:
        # manual addition starting from the LSB to the MSB while holding a carry

        # represent negative numbers as two's complement representation 
        # by wrapping them around through adding 2 ** 32. That would make their
        # MSB (32nd bit) 1 representing that they are negative numbers 
        if a < 0: a += 2 ** 32
        if b < 0: b += 2 ** 32
        
        a, b = str(bin(a))[2:], str(bin(b))[2:]

        m = max(len(a), len(b))
        # equalize the number of bits they have
        if len(a) < m: a = "0" * (m - len(a)) + a
        if len(b) < m: b = "0" * (m - len(b)) + b

        ans = ["0" for _ in range(m)]

        carry = 0
        for i in reversed(range(m)):
            x, y = a[i], b[i]
            if x == "0" or y == "0":
                if x == "1" or y == "1":
                    if carry:
                        ans[i] = "0"
                    else:
                        ans[i] = "1"
                else:
                    if carry:
                        ans[i] = "1"
                        carry = 0
                    else:
                        ans[i] = "0"
            else:
                if carry:
                    ans[i] = "1"
                else:
                    ans[i] = "0"
                    carry = 1

        if carry:
            ans = ["1"] + ans

        ans = int("".join(ans), 2)
        # the answer could have well gone past 2**31 meaning it is negative
        # so we need to bring it back to its negative number representation
        while ans >= 2 ** 31 - 1:
            ans -= 2 ** 32
            
        return ans
