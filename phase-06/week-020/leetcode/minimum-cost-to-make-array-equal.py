class Solution:
    def smallestNumber(self, pattern: str) -> str:
        # backtracking
        res = "9" * (10)

        def check(s, pattern):
            for i in range(len(s) -1):
                if pattern[i] == "I":
                    if s[i] > s[i + 1]:
                        return False

                else:
                    if s[i] < s[i + 1]:
                        return False

            
            return True

        def dfs(ind, s, used):
            nonlocal res
            if ind == len(pattern) + 1:
                if check(s, pattern):
                    res = min(res, s)

                    return

            for i in range(1, 10):
                if i not in used:
                    if check(s, pattern):
                        used.add(i)
                        dfs(ind + 1, s + str(i), used)
                        used.discard(i)

            
        dfs(0, "", set())

        return res
        
