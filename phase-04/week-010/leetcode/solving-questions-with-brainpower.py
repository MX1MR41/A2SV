class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # dp
        # start from the last index, and for every index i with points p and skip s,
        # you have the ability to earn p and any maximum p from indices starting from i + s + 1,
        # or just skip it and get the immediately next index's previous computed score
        # choose whichever is maximum

        n = len(questions)

        dp = [0] * n
        dp[-1] = questions[-1][0]

        for i in range(n - 2, -1, -1):
            points, skip = questions[i]
            nxt = i + skip + 1

            if nxt < n:
                points += dp[nxt]

            dp[i] = max(dp[i + 1], points)


        return max(dp)


