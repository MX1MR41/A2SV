class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # backtracking
        letters = ['a', 'b', 'c']
        

        res = []
        def dfs(s):
            if len(s) == n:
                res.append(s)
                return

            
            for i in letters:
                if s and s[-1] == i:
                    continue

                dfs(s + i)

                if len(res) >= k:
                    return

        dfs("")

        return res[k - 1] if len(res) >= k else "" 
        
