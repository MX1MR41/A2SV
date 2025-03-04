class Solution:
    def checkPowersOfThree(self, n: int) -> bool:

        # backtracking
        # try subtracting different powers of three from the number until it becomes 0
        
        def dfs(n, p):
            if n == 0:
                return True

            if n < 0 or p > 16:
                return False

            return dfs(n - pow(3, p), p + 1) or dfs(n, p + 1)

        return dfs(n, 0)

        
        

        
        
