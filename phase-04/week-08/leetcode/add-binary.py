# one-liner
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a, 2) + int(b, 2)))[2:]

# longer manual solution
  
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        na, nb = len(a), len(b)
        l = max(na, nb)
        #append extra zeros at the front of the shorter addend to make it equal in length
        if na > nb:
            b = "0" * (na - nb) + b
        elif nb > na:
            a = "0" * (nb - na) + a
        # convert to lists for ease of manipulation
        a, b = list(a), list(b)
        ans = ['0'] * (max(na, nb) + 1)
        # our iterator needs to go from right to left so -1, -2, -3, ...
        j, carry = -1, 0

        for _ in range(l):
            p , q = a[j], b[j] # the current addend single digits
            if p == "1" and q == "1":
                if carry:
                    ans[j] = "1"
                else:
                    ans[j] = "0"
                    carry = 1
            elif p == "0" and q == "0":
                if carry:
                    ans[j] = "1"
                    carry = 0
                else:
                    ans[j] = "0"
            else:
                if carry:
                    ans[j] = "0"
                else:
                    ans[j] = "1"

            j -= 1

        if carry: # if we stuill have a carry at the end, we need to update accordingly
            ans[j] = "1"

        zero = 0
        for i in ans[:-1]:
            if i != "0":
                break

            zero += 1

        return "".join(ans[zero:])
