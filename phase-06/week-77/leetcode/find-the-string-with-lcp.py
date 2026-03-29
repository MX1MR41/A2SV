class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        # dp
        # assume matrix is valid and build the lexicographically smallest string 
        # based on matching which indices have lcp > 0
        # then compare built string with the lcp matrix by checking if the problem can be built
        # from the subproblem, i.e. lcp[i][j] == 1 + (lcp[i + 1][j + 1]) if string[i] == string[j]
        n = len(lcp)
        res = [""] * n
        curr_char = ord("a")

        for i in range(n):
            if res[i]:
                continue

            if curr_char > ord("z"):
                return ""

            res[i] = chr(curr_char)

            for j in range(i + 1, n):
                if lcp[i][j] > 0:
                    res[j] = chr(curr_char)

            curr_char += 1

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                expected_lcp = 0

                if res[i] == res[j]:
                    expected_lcp = 1 + (
                        lcp[i + 1][j + 1] if i + 1 < n and j + 1 < n else 0
                    )

                if lcp[i][j] != expected_lcp:
                    return ""

        return "".join(res)
