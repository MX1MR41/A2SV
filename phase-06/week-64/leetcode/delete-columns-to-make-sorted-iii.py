
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        string_length = len(strs[0])

        dp = [1] * string_length

        for current_col in range(string_length):

            for prev_col in range(current_col):

                if all(string[prev_col] <= string[current_col] for string in strs):

                    dp[current_col] = max(dp[current_col], dp[prev_col] + 1)

        return string_length - max(dp)
