class Solution:
    def decodeString(self, s: str) -> str:
        # a dictionary to map the string version of the numbers to the int version
        lookup = {str(i):i for i in range(1,301)} 
        
        def rec(s):
            if "[" not in s: # Tthe base case; if s is only letters, return it
                return s

            n, i, curr = len(s), 0, ""
            while i < n:
                if s[i] in lookup:
                    openBracket = i + 1
                    # find the index of the first bracket; 
                    # to get all the digits of the multiplier
                    while openBracket < n and s[openBracket] != "[":
                        openBracket += 1
                    # multiplier
                    mul = int(s[i:openBracket]) 
                    cnt = 1
                    closedBracket = openBracket + 1
                    start = openBracket + 1
                    # find the next closing bracket
                    # to be more precise, the index just after the appropriate
                    # closing bracket
                    while closedBracket < n and cnt:
                        if s[closedBracket] == "[":
                            cnt += 1
                        elif s[closedBracket] == "]":
                            cnt -= 1
                        closedBracket += 1
                    # recursively do the same for the string inside the bracket
                    curr += mul * rec(s[start:closedBracket-1]) 
                    i = closedBracket
                    
                elif s[i] != '[' and s[i] != ']':
                    curr += s[i]
                    i += 1

            return curr

            

        return rec(s)

            