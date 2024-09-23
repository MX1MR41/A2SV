class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # dynamic programming
        # use two loops to iterate over all combinations 
        # store the maximum length of a valid word that has occured before 
        # the current index; trickle down the greatest answer seen so far

        dictionary = set(dictionary)
        n = len(s)
        dp = [0] * (n + 1)

        for start in range(n):
            if start >= 1:
                dp[start] = max(dp[start], dp[start - 1])

            for end in range(start + 1, n + 1):
            
                if s[start:end] in dictionary:

                    length = end - start
                    dp[end] = max(dp[end], dp[start] + length)

        return n - max(dp)
