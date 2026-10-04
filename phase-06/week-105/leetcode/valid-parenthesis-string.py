class Solution:
    def checkValidString(self, s: str) -> bool:
        #  stack

        star = []
        used = set()
        op = 0
        n = len(s)
        for i in range(n):
            if s[i] == "*":
                star.append(i)

            elif s[i] == "(":
                op += 1

            else:
                if op == 0:
                    if not star:
                        return False

                    used.add(star.pop())

                else:
                    op -= 1

        star = []
        cl = 0
        for i in range(n - 1, -1, -1):
            if s[i] == "*":
                if i not in used:
                    star.append(i)

            elif s[i] == ")":
                cl += 1

            else:
                if cl == 0:
                    if not star:
                        return False

                    used.add(star.pop())

                else:
                    cl -= 1

        return True
