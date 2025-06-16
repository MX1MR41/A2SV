class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # top-down dp
        # decompress the pattern so that instead of a*b it will be [(a, True), (b, False)]
        # True for can be used or skipped or reused, and False for can't be skipped and
        # must be used and can't be reused. Then it is a simple choose or not choose dfs

        pat = []
        i = 0
        while i < len(p):
            if i + 1 < len(p):
                if p[i + 1] == "*":
                    pat.append((p[i], True))
                    i += 2
                else:
                    pat.append((p[i], False))
                    i += 1

            else:
                pat.append((p[i], False))
                i += 1

        p = pat

        dp = dict()

        lens = len(s)
        lenp = len(p)


        # return True if s[i:] can be matched with p[j:], False otherwise
        def match(i, j):
            
            # already computed, no need to re-compute
            if (i, j) in dp:
                return dp[(i, j)]

            # completed matching the whole string with the whole pattern
            if i >= lens and j >= lenp:
                return True
            
            # finsihed the pattern but string is not finished
            if (i < lens and j >= lenp):
                return False


            # finished the string but the pattern is not finished
            if (i >= lens and j < lenp):

                if p[j][1] == True: # a skippable character, so let's skip it and try next
                    return match(i, j + 1)
                
                else:
                    return False


            can = False # s[i:] can be matched with p[j:]

            for b in range(j, lenp):

                if s[i] == p[b][0]: # a chracter match

                    if p[b][1]: # if skippable and reusable try both options
                        
                        temp = match(i + 1, b) or match(i + 1, b + 1)
                        if temp:
                            can = True
                            break

                    else: # cannot  be reused nor skipped, so use it once and move on
                        
                        temp = match(i + 1, b + 1)
                        if temp:
                            can = True
                            break

                elif p[b][0] == ".": # potntial match with any character

                    if p[b][1]: # skippable/reusable, so try both options
                        
                        temp = match(i + 1, b) or match(i + 1, b + 1)
                        if temp:
                            can = True
                            break
                    
                    else: # cannot  be reused nor skipped, so use it once and move on
                        
                        temp = match(i + 1, b + 1)
                        if temp:
                            can = True
                            break
                
                # if current pattern character cannot be matched and cannot be skipped,
                # we stop here since further matching is impossible
                if not p[b][1]: 
                    break


            dp[(i, j)] = can # store for later
            
            return can



        return match(0, 0)
