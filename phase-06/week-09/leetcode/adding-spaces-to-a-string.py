class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces.sort()
        n_spaces = len(spaces)
        res = ""
        n_s = len(s)
        curr_space = 0
        for i in range(n_s):
            if curr_space < n_spaces and i == spaces[curr_space]:
                res += " "
                curr_space += 1
            
            res += s[i]

        return res
        
