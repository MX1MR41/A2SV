# DYNAMIC PROGRAMMING ONLY SOLUTION O(N2)
class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        # dynamic programming 
        # for every fruit that we can get as a reward, we take it as a reward only if that fruit's
        # reward itself is not worth taking.
        # so for every fruit purchase, we need to be careful of which reward fruits  we can take.
        # let dp[i] be the minimum cost of buying all fruits from i to n
        # dp[i] = prices[i] + min(dp[j + 1]) for every j'th fruit we can get as a reward, and the 
        # reason we take the dp[j + 1] instead of dp[j] is because we assume that if we get the j'th
        # fruit as a reward the rest of the cost we must incur is dp[j + 1]

        n = len(prices)

        dp = [float("inf")] * n # initialize as maximums to be minimized

        dp[-1] = prices[-1] # set the base case: the last fruit must be bought if it is alone

        dp.append(0) # append 0 at the end for padding purpose

        for i in range(n - 2, -1, -1):
            # iterate over every possible reward fruit
            for j in range(i, min(n, 2*i + 2)):

                # buying the i'th fruit and taking all fruit's upto j'th as a reward
                # and incurring the cost of buying the other fruits starting from (j+1)'th separately
                dp[i] = min(dp[i], prices[i] + dp[j + 1])



        return dp[0]


# DP + MONOTONIC QUEUE O(N)
class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        # dynamic programming + monotonic queue
        # refer to the dp solution for the definitions and purposes of the dp part
        # we want to get the smallest dp from a list of possible reward-able fruits
        # we can use a monotonic queue that will store the smallest dp value at the front
        # and we can prune invalid entries from the front using the popleft functionality
        n = len(prices)
        dp = [float("inf")] * n
        dp[-1] = prices[-1]
        dp.append(0)

        que = deque([(n, 0)])
        for i in range(n - 1, -1, -1):

            # the intial dp solution
            # for j in range(i, min(n, 2*i + 2)):
            #     dp[i] = min(dp[i], prices[i] + dp[j + 1])

            # remove invalid entries from the front, i.e. entries which are beyond dp[j + 1]
            # where j is a fruit we can get as a reward and dp[j + 1] is the cost of buying the 
            # rest of the fruits if we took upto j'th as a reward
            while que and que[0][0] > 2*i + 2:
                que.popleft()

            dp[i] = prices[i] + que[0][1] # get the smallest dp

            # keep the monotonicity
            while que and que[-1][-1] > dp[i]:
                que.pop()

            que.append((i, dp[i]))


        return dp[0]
        
        
