class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for i in tokens:
            if i == "+":
                b, a = stk.pop(), stk.pop()
                stk.append(a + b)            
            elif i == "-":
                b, a = stk.pop(), stk.pop()
                stk.append(a - b)
            elif i == "*":
                b, a = stk.pop(), stk.pop()
                stk.append(int(a * b))
            elif i == "/":
                b, a = stk.pop(), stk.pop()
                c = a / b
                if c < 0:
                    c = ceil(a/b)
                else:
                    c = a // b
                stk.append(c)
            else:
                stk.append(int(i))

        return stk.pop()


        