class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # recursion + dp
        if not s1 and not s2 and not s3: return True

        m, n = len(s1), len(s2)
        if len(s3) != m + n: return

        dp = defaultdict(bool)
        def backtrack(index, s, a, b):

            if (a, b) in dp:
                return dp[(a, b)]

            if s == s3 and len(s) == m + n:
                dp[(a, b)] = True
                return True


            need = s3[index]
            if a < m and s1[a] == need:
                if backtrack(index + 1, s + need, a + 1, b):
                    dp[(a, b)] = True
                    return True

            if b < n and s2[b] == need:
                if backtrack(index + 1, s + need, a, b + 1):
                    dp[(a, b)] = True
                    return True

            dp[(a, b)] = False


        return backtrack(0, "", 0, 0)


            


        
