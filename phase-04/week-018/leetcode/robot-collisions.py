class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        # sort by positions then simulate the process using stack

        # all robots move in the same direction, hence no colisions at all
        if "L" not in directions or "R" not in directions:
            return healths
        
        # store the original indices of the positions of the robots for later 
        original = {x:ind for ind, x in enumerate(positions)}

        arr = []
        for i in range(len(positions)):
            arr.append((positions[i], healths[i], directions[i]))

        arr.sort() # sort by positions

        right = [] # a stack to store the robots that move right
        left = [] # a stack to store the surviving robots that move left

        for p, h, d in arr: # position, health and direction
            if d == "R":
                right.append((p,h,d))
            # we store the rights and we process the lefts we encounter
            else:
                while right:
                    last_p, last_h, last_d = right.pop()

                    if last_h > h:
                        h = -1 # mark it as dead
                        last_h -= 1
                        right.append((last_p,last_h,last_d))
                        break

                    elif last_h < h:
                        h -= 1 # decrease 1 from the health

                    else:
                        h = -1
                        break
                # if it still survives      
                if h > 0:
                    left.append((p,h,d))

        ans = right + left
        # sort by original indices in positions
        ans.sort(key = lambda x: original[x[0]])
        
        return [x[1] for x in ans]

        
