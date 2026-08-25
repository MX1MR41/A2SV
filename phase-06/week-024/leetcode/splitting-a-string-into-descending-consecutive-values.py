class Solution:
    def splitString(self, s: str) -> bool:
        # backtracking + pruning

        n = len(s)

        def dfs(i, curr):
            if i == n:
                return len(curr) >= 2



            for j  in range(i + 1, n + 1):
                num = int(s[i:j])
                # if the current num isn't exactly -1 of the previous num, we prune this path
                if curr and num - curr[-1] != -1:
                    continue

                curr.append(num)

                if dfs(j, curr):
                    return True

                curr.pop()

            return False


        for i in range(1, n):
            if dfs(i, [int(s[:i])]):
                return True

        return False
