class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        # approach works by iterating through the string and if we find
        # a lone letter, we recursively explore the left and right 
        # to find the longest nice substring

        def nice(sub):
            # base case, an empty string
            if not sub:
                return ""

            for i in range(len(sub)):
                # if the current letter is a lone element
                if sub[i].swapcase() not in sub:
                    r = nice(sub[i+1:])
                    l = nice(sub[:i])
                    
                    # if there are no nice strings on either side
                    if not r and not l:
                        return ""
                    
                    # return the longest nice string
                    if len(l) >= len(r):
                        return l
                    else:
                        return r
                    

            # if itself is nice then return it
            return sub

        return nice(s)


                
        