class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        # recursion
        # same logic as decode string https://leetcode.com/problems/decode-string/description/
        exp = expression
        n = len(expression)
        res = set()
        curr = set()

        i = 0
        while i < n:

            if exp[i] == "{":
                opened = 1
                j = i + 1
                while j < n and opened > 0:
                    if exp[j] == "{":
                        opened += 1
                    elif exp[j] == "}":
                        opened -= 1

                    j += 1

                got = self.braceExpansionII(expression[i + 1 : j - 1])

                if not curr:
                    curr = set(got)
                else:
                    newcurr = set()
                    for c in curr:
                        for g in got:
                            newcurr.add(c + g)

                    curr = newcurr

                i = j

            elif exp[i] == ",":
                res = res.union(curr)
                curr = set()
                i += 1

            else:
                if not curr:
                    curr.add(exp[i])
                else:
                    newcurr = set()
                    for c in curr:
                        newcurr.add(c + exp[i])

                    curr = newcurr

                i += 1

        res = res.union(curr)

        return sorted(list(res))
