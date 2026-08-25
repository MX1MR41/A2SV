class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        ans, n = 0, len(flips)
        i, j = 1,1 # i is iteration and j is leftmost 0 bit
        flipped = set() # set t contain the flipped bits

        while i < n + 1:
            f = flips[i-1] # the flipped bit in this iteration of i
            flipped.add(f)
            # if f happens to be the leftmost 0 bit, we'll find the next leftmost
            if f == j: 
                while j in flipped:
                    j += 1
                # if the the leftmost 0 bit is beyond the current ith step, then pre-aligned
                if j > i:
                    ans += 1

            i += 1

        
        return ans

            

            
            
        