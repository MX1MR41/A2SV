class Solution:
    def isValid(self, s: str) -> bool:
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
        