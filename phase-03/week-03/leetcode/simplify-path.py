class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split("/")
        stk = []
        res = ""
        for i in dirs:
            if not i or i == ".":
                continue
            elif i == "..":
                if not stk:
                    continue
                stk.pop()
            else:
                stk.append(i)

        return  "/"+"/".join(stk)
        