class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp
        # create a dp array that will be populated by boolean values
        # dp[i] is true if s could be formed upto i - 1 in any combination of possible words
        # then for every dp[i] that is true, we check every string from i + 1 to j
        # where j goes to n. If a valid word is found, we set dp[j] as true
        words = set(wordDict)
        n = len(s)

        dp = [False for _ in range(n)]

        for i in range(n):
            if s[: i + 1] in words:
                dp[i] = True

        for i in range(n):
            if dp[i]:

                for j in range(i + 1, n):
                    if s[i + 1 : j + 1] in words:

                        dp[j] = True

        return dp[-1]
