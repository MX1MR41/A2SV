class Solution:
    def __init__(self):
        self.res = []


    def restoreIpAddresses(self, s: str) -> List[str]:
        def check(s):
            if s.count(".") != 3:
                return False

            s = s.split(".")

            for i in s:
                if not i or (i[0] == "0" and len(i) > 1) or int(i) > 255:
                    return False

            return True

        n = len(s)


        def backtrack(ind, curr, dots):
            if ind == n:
                if check(curr):
                    self.res.append(curr)

                return

            backtrack(ind + 1, curr + s[ind], dots)
            if dots:
                backtrack(ind, curr + ".", dots - 1)



        backtrack(0, "", 3)
        return self.res
        
