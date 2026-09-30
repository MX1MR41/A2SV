class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        # stack
        a_stk = []
        b_stk = []
        a_d = b_d = 0

        res = []
        n = len(seq)
        for i in range(n):

            if seq[i] == "(":
                if not a_stk:
                    a_stk.append("(")
                    a_d += 1
                    res.append(0)
                    continue

                if not b_stk:
                    b_stk.append("(")
                    b_d += 1
                    res.append(1)
                    continue

                if a_d <= b_d:
                    a_stk.append("(")
                    a_d += 1
                    res.append(0)
                    continue
                else:
                    b_stk.append("(")
                    b_d += 1
                    res.append(1)
                    continue

            else:

                if not a_stk or a_stk[-1] == ")":

                    b_stk.pop()
                    b_d -= 1
                    res.append(1)
                    continue

                if not b_stk or b_stk[-1] == ")":

                    a_stk.pop()
                    a_d -= 1
                    res.append(0)
                    continue

                if a_d >= b_d:

                    a_stk.pop()
                    a_d -= 1
                    res.append(0)
                    continue
                else:

                    b_stk.pop()
                    b_d -= 1
                    res.append(1)
                    continue

        return res


