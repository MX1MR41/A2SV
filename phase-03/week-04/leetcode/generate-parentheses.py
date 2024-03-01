class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # modified code from Valid Parentheses question
        # https://leetcode.com/problems/valid-parentheses/
        
        # function to validate paretheses
        def isValid(s: str):
            stk = []
            pars = {"}":"{", ")":"(", "]":"["}
            for i in s:
                if i not in pars:
                    stk.append(i)
                else:
                    if not stk or stk[-1] != pars[i]:
                        return False
                    stk.pop()
            return True if not stk else False


        def gen(i, comb, o, c):
            if i >= 2*n:
                p = "".join(comb)
                if isValid(p):
                    res.append("".join(comb))
                return

            # pruning case; if the number of closing exceeds openings
            # or either of the brackets exceeds n
            if c > o or o > n or c > n: 
                return 

            
            comb.append(")")
            gen(i+1, comb, o, c+1)
            comb.pop()

        
            comb.append("(")
            gen(i+1, comb, o+1, c)
            comb.pop()

        res = []

        gen(0,[],0,0)

        return res

            
        