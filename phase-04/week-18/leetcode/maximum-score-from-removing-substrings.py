class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # do a two-pass with first the higher score then the lower score
        
        if x > y:
            remove = "ab"
        else:
            remove = "ba"

        stk = []
        score = 0

        for i in s:
            if stk and stk[-1] + i == remove:
                stk.pop()
                score += max(x,y)
            else:
                stk.append(i)

        remove = remove[::-1]

        s = "".join(stk)
        stk = []
        for i in s:
            if stk and stk[-1] + i == remove:
                stk.pop()
                score += min(x,y)
            else:
                stk.append(i)

        return score
        
