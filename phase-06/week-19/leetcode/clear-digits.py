class Solution:
    def clearDigits(self, s: str) -> str:
        stk = []
        digits = set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
        for i in s:
            if i in digits:
                if stk:
                    stk.pop()

            else:
                stk.append(i)

        return "".join(stk)
