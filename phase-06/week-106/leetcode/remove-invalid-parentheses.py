class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        # backtracking
        

        res = set()
        n = len(s)

        def dfs(par, i, op):
            if i == n:
                if op == 0:
                    res.add(par)
                return 

            
            if s[i] == "(":
                
                dfs(par + s[i], i + 1, op + 1)
                dfs(par, i + 1, op)
            elif s[i] == ")":
                if op > 0:
                    dfs(par + s[i], i + 1, op - 1)

                dfs(par, i + 1, op)
            else:
                dfs(par + s[i], i + 1, op)

        
        dfs("", 0, 0)

        res = sorted(list(res), key = lambda x: -len(x))

        max_len = len(res[0])
        final_res = []
        for i in res:
            if len(i) < max_len:
                break

            final_res.append(i)

        return final_res


        return list(res)

