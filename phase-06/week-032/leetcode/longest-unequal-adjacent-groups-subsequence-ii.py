class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        # dp
        # build a two-dimensional dp matrix where matrix_dp[i][j] == True if the 
        # hamming distance between words[i] and words[j] is equal to 1 and 
        # groups[i] != groups[j]. If either of the conditions doesn't hold, then dp[i][j] = False.
        # compute the lengths of the longest subsequences ending at i for each i in [0...n]
        # and store in dp array. For every i, keep track of the best previous index which has
        # the longest valid subsequence length. Use that data to rebuild the subsequence.

        def hamming(word1, word2):
            hams = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    hams += 1

            return hams


        n = len(words)
        
        if n == 1:
            return words


        matrix_dp = [[False for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if len(words[i]) == len(words[j]):
                    hams = hamming(words[i], words[j])

                    if hams == 1 and groups[i] != groups[j]: # possible neighbors in subsequence
                        matrix_dp[i][j] = True


        dp = [1] * n

        prev = {i: i for i in range(n)} # store the best previous subsequence neighbor for each i

        best_dp, best_end = 0, -1

        for i in range(1, n):
            best_prev_dp, best_prev = 0, i

            # from all the previous indices, find an index that can be a neighbor and has best dp
            for j in range(i):

                if matrix_dp[i][j]: # possible neighbor

                    if dp[j] > best_prev_dp: # possible best neighbor

                        best_prev_dp = dp[j]
                        best_prev = j

            prev[i] = best_prev # assign the best previous index as the parent or previous nei
            dp[i] += best_prev_dp # add the length of that best nei to the length of i which was 1

            if dp[i] > best_dp: # i will become the chosen end for the longest valid subsequence
                best_dp = dp[i]
                best_end = i


        res = []

        # move up the tree, or backwards, while gathering the ancestors, or previous neighbors
        while best_end != prev[best_end]:

            res.append(words[best_end])

            best_end = prev[best_end]
            

        res.append(words[best_end]) # append one more time for the root

        res.reverse() # reverse, since we built the subsequence in reverse

        return res


                



        
        
