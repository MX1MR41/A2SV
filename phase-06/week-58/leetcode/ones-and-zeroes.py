class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # dynamic programming
        # this problem is an 0/1 knapsack problem where the weights are
        # the number of zeros and ones in a subset, and the values are the number
        # of subsets that can have z zeros and o ones
        # TIP: for 0/1 knapsack iterate backwards to avoid double contributions
        # for unbounded knapsack iterate forwards

        
        s = len(strs)

        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
  

        for i in range(s):
            string = strs[i]
            ones, zeros = string.count("1"), string.count("0")

            # iterate backwards from the end and compute for the new subsets 
            for z in range(m, -1, -1):
                for o in range(n, -1, -1):

                    if ones + o > n or zeros + z > m:
                        continue


                    if dp[z][o] > 0: 
                        
                        subs = dp[z][o] + 1
                        dp[zeros + z][ones + o] = max(dp[zeros + z][ones + o], subs)
                    

            # base case
            if zeros <= m and ones <= n:
                dp[zeros][ones] = max(dp[zeros][ones], 1)

 
        res = max(max(d) for d in dp)
        return res

