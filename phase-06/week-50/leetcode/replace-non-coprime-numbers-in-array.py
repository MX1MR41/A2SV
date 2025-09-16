class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        # stack + math
        # a * b = lcm(a * b) * gcd(a * b)
        # move from left to right and simulate the process using a stack

        stack = []
        for i in nums:

            num1 = i
            while stack and gcd(num1, stack[-1]) != 1:
                num2 = stack.pop()

                g = gcd(num1, num2)

                lcm = (num1 * num2) // g
                num1 = lcm

            stack.append(num1)

        return stack
