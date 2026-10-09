class Solution:
    def minInsertions(self, s: str) -> int:

        res = op = cl = 0
        pair = 0
        for i in s:

            if i == "(":
                if pair == 1:
                    res += 1
                    if op > 0:
                        op -= 1
                    else:
                        res += 1
                    pair = 0
                op += 1
            else:
                pair += 1
                if pair == 2:
                    if op == 0:
                        res += 1
                    else:
                        op -= 1

                    pair = 0

        if pair == 1:
            if op == 0:
                res += 2
            else:
                res += 1
                op -= 1

        res += 2 * op

        return res
