class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        wordDict = set(wordDict)

        n = len(s)

        dp = [[] for _ in range(n)]
        # dp[i] all possible formation upto index i


        for i in range(n):
            for j in range(i, 0, -1):

                substring = s[j: i + 1]
                if substring not in wordDict:
                    continue


                for formation in dp[j - 1]:
                    new_formation = formation + [substring]
                    dp[i].append(new_formation)


            substring = s[:i + 1]
            if substring in wordDict:
                dp[i].append([substring])



        res = []

        for formation in dp[-1]:
            res.append(" ".join(formation))

        return res




        
