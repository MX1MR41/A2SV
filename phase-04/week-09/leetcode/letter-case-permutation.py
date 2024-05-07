class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        # backtracking with bit manipulation
        # use a bitmask to keep track of the already processed bits 
        # initially assign all letters a bit of 0 in the bitmask
        # and after we process that letter we flip its bit on
        n = len(s)
        mask = 0

        for i in range(n):
            if not s[i].isalpha():
                mask |= 1<<i


        def dfs(s, mask):
            nonlocal ans
            
            for i in range(n):
                # there exists a letter in the string that hasnt been processed yet
                if not mask & 1 << i:
                    break
            else:
                # the string has been processed completely
                ans.append(s)
                return


            for i in range(n):
                if not mask & 1 << i:
                    new = s[:i] + s[i].swapcase() + s[i+1:]
                    mask |= 1<<i # processed, hence flip its bit on
                    # backtrack on both
                    dfs(s, mask)
                    dfs(new, mask)
                    
                    # break because the remaining unprocessed letters will
                    # be processed in the dfs
                    break

            

        ans = []
        dfs(s, mask)

            
        return ans
        
