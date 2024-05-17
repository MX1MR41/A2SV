class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # solution uses two dp arrays dp and dp2
        # dp[i] will store the processed result of questions[i]
        # dp2[i] will store the maximum result seen so far from i to the end of the array
        # when processing result for dp[i], the answer will be the maximum of solving i'th question
        # plus solving the most available next question OR solving i'th question plus solving ANY other
        # available question upto the end of the array. For that we need to know the maximum available
        # score from all available questions; hence dp2.
        n = len(questions)
        if n <= 2: return max([i[0] for i in questions])

        dp = dp2 = [0] * (n)

        dp[-1] = dp2[-1] = questions[-1][0]

        dp[-2] = questions[-2][0]

        dp2[-2] = max(dp2[-1], dp[-2])



        for i in reversed(range(n-2)):
            curr, skip = questions[i]
            nxt = i + skip + 1
            if nxt < n:
                if nxt < n - 1:
                    dp[i] = max(curr + dp[nxt], curr + dp2[nxt+1])
                else:
                    dp[i] = curr + dp[nxt]
            else:
                dp[i] = curr

            dp2[i] = max(dp[i], dp2[i+1])

            

        return max(dp)
        
