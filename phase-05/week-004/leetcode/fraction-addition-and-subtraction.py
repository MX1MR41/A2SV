class Solution:
    def fractionAddition(self, expression: str) -> str:
        def simplify(a,b):
            for i in reversed(range(1, 10)):
                if not a % i and not b % i:
                    a //= i
                    b //= i
                    

            return (a, b)

            

        if expression[0] != "-":
            expression = "+" + expression
        
        nums = []

        ind = 1
        last = 0
        n = len(expression)



        while ind < n:
            if expression[ind] == "-" or expression[ind] == "+":

                nums.append(expression[last:ind])
                last = ind
            ind += 1

        nums.append(expression[last:])
        arr = []
        for num in nums:
            a, b = list(map(int, num.split("/")))
            arr.append([a,b])

        lcm = math.lcm(*[a[-1] for a in arr])

        numerator = 0
        denominator = lcm

        for a, b in arr:
            a *= lcm/b
            b = lcm

            numerator += a

        ans = simplify(numerator, denominator)


        return str(int(ans[0])) + "/" + str(int(ans[1]))
