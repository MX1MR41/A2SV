class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        first = {} # store the first indices of each element
        for i in range(n):
            if s[i] not in first:
                first[s[i]] = i
            
        last = {} # store the last indices of each element
        for i in range(n):
            last[s[i]] = i


        l, r = 0, 0 # left and right pointers of each partition
        # a counter for elements who havent reached their last indices yet 
        #and a set to store the elements seen so far
        nonEnd, seen = 0, set() 
        res = []

        while r < n:
            j = s[r]
            if r == last[j]:
                if last[j] != first[j]: # we deduct nonEnd only if the current element isnt an only element
                    nonEnd -= 1

                if not nonEnd: # if there are no more elements before it who havent met theor last indeies
                    res.append(r - l + 1)
                    l = r + 1
                
            else:
                if j not in seen: # the set helps with avoiding over decreasing the nonEnd
                    nonEnd += 1

            seen.add(j)

            r += 1
            
        return res






        
            
        