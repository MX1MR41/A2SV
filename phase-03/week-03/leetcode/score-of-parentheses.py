class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = []
        score = 0   

        for par in s:
            if par == "(":
                stk.append(score)
                score = 0
            elif par == ")":
                last_score = stk.pop()
                score = last_score + max(2 * score, 1)


        return score
