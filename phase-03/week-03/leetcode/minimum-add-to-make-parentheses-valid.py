class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openers = 0 # count of unclosed opening parenthesis
        closers = 0 # count of closing parenthesis with no openers available 

        for i in s:

            if i == "(":
                openers += 1 # since we havent found a closing for this one yet

            else:
                # since one closer matches one opener; one less opener available
                openers -= 1 

                if openers < 0: # indicates that the current closer has no available opener
                    closers += 1
                    openers = 0

        
        return openers + closers
        