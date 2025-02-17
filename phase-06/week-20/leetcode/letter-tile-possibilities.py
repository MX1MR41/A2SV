class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # backtracking
        res = set()
        n = len(tiles)
        tot = 0


        def dfs(ind, s, used):
            if ind == n:
                res.add(s)
                return

            if s:
                res.add(s)

            for i in range(n):
                if i not in used:
                    s += tiles[i]
                    used.add(i)
                    dfs(ind + 1, s, used)
                    s = s[:-1]
                    used.discard(i)

        dfs(0, "", set())

        return len(res) 
