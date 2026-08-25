class Solution:
    def makeFancyString(self, s: str) -> str:
        stk = []
        for i in s:
            if len(stk) >= 2 and stk[-1] == i and stk[-2] == i:
                continue
            else:
                stk.append(i)

        return "".join(stk)
        
