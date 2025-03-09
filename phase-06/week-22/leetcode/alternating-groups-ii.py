class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        # sliding window
        # start from a window of size 1 and keep expanding while valid window until 
        # you reach size k. From then on it will be a fixed sliding window while the
        # group/window is valid, else restart the process.
        
        res = 0
        n = len(colors)

        # initialize the left and right pointers
        left = 0
        right = 1

        size = 1 # start with a single element, window of size 1

        colors += colors # double the array to simulate circularity

        # traverse until the left (the start of the window) tries every index 
        # in the original colors array (before it was doubled)
        # so that our window will simulate every tile as a starting point for window
        while left < n:
            
            # invalid neighbor tiles found, reset window and pointers
            if colors[right] == colors[right - 1]:
                left = right
                right += 1
                size = 1

            else:
                # the previously moved right pointer was valid, so we increase size by 1
                # if it hasn't yet reached k
                if size < k: 
                    size += 1

                if size == k: # if k has been reached, we found a valid group
                    res += 1
                    # slide the fixed window by one unit
                    right += 1
                    left += 1
                else:
                    # if k hasn't been reached, we expand our right pointer to be 
                    # checked in the next iteration if the expanded window is valid
                    right += 1


        return res

        
