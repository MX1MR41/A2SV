class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def dfs(i, comb):
            # base case: return if we have found a valid combination, 
            # we append it to our answer and return
            if len(comb) == k:
                ans.append(comb[:])
                return

            for j in range(i+1, n+1):
                # we keep appending until we reach the length of k making it a valid combo
                comb.append(j)
                # immediately we also keep appending the next elements till length k
                # and valididty is reached
                dfs(j, comb)
                # the function above returns back only if it has found a valid combo
                # i.e the length k has been reached. In that case, we pop the last element
                # and we explore the next possible combinations
                comb.pop()

        dfs(0,[]) # starting from zero, but zero will not be appended, the appending starts from 1

        return ans

                    
            
                
        