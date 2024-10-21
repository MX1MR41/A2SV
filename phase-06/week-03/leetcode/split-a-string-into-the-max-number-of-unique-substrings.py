class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        ans = 0

        n = len(s)

        def dfs(ind, uniq, seen):
            nonlocal ans
            if ind == n:
                seen.add(uniq)
                ans = max(ans, len(seen))
                return

            
            dfs(ind + 1, uniq + s[ind], seen.copy())
            seen.add(uniq)
            dfs(ind + 1, s[ind], seen)


        dfs(1, s[0], set())

        return ans
