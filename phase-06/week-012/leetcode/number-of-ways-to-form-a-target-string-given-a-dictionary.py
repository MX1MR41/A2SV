class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        # dp + prefix sum
        # create a counter of each letters at each index
        # map[index][letter] = <count of that letter's appearance at that index>
        # create a 2D table to perform dynamic programming and prefix summing on
        # dp[i][j][0] = count of target[j]'th letter at word[i] for every word
        # dp[i][j][1] = total possible ways to form target upto jth index
        # dp[i][j] = [count of letter at i index, total ways to make target upto j index]
        # base case: initialize the total ways for the first letter the same as its count,
        # and sum up downwards the total number of ways to form the 1st letter 
        # then for every (i, j) dp[i][j][1] = dp[i][j][0] * dp[i-1][j-1][1]
        # i.e. total ways = count of jth letter * number of ways to form (j-1)th letter
        # for every column iteration, adter doing the dynamic programming, sum up the ways
        # downwards to the bottom-most will have the total ways to form target upto j
        # summary: dp diagonally, prefix sum downwards

        
        count = defaultdict(dict)
        n = len(words[0])
        for i in range(n):
            for word in words:

                if word[i] in count[i]:
                    count[i][word[i]] += 1

                else:
                    count[i][word[i]] = 1

        m = len(target)

        dp = [[[0, 0] for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):

                letter = target[j]

                if letter in count[i]:
                    dp[i][j][0] = count[i][letter]

                    if j == 0:
                        dp[i][j][1] = dp[i][j][0]

        for i in range(1, n):
            dp[i][0][1] += dp[i - 1][0][1]


        for j in range(1, m):
            for i in range(1, n):
                dp[i][j][1] = (dp[i][j][0] * dp[i-1][j-1][1]) 

            for i in range(j + 1, n):
                dp[i][j][1] += dp[i - 1][j][1]


        return dp[-1][-1][-1] % (10**9 + 7)
