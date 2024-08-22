class Solution:
    def strangePrinter(self, s: str) -> int:
        # dp[i][j] represents the minimum turns to for s from i to j
        n = len(s)

        dp = [[float("inf")] * n for _ in range(n)]

        # start from the end
        for start in reversed(range(n)):
            # it takes one turn to make one letter
            dp[start][start] = 1

            for end in range(start + 1, n):
                # if the first and last are the same, we "ignore" the last
                if s[start] == s[end]:
                    dp[start][end] = dp[start][end - 1]
                else:
                    # If they are different, find the minimum number of turns needed
                    # to print the substring by splitting it at different points (k)
                    for split_point in range(start, end):
                        # The number of turns is the sum of printing both substrings separately
                        dp[start][end] = min(
                            dp[start][end],
                            dp[start][split_point] + dp[split_point + 1][end],
                        )

        return dp[0][-1]
