class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s2 = list(s2)

        if s1 == s2:
            return True

        s1[0], s1[2] = s1[2], s1[0]

        if s1 == s2:
            return True

        s1[0], s1[2] = s1[2], s1[0]
        s1[1], s1[3] = s1[3], s1[1]

        if s1 == s2:
            return True

        s1[0], s1[2] = s1[2], s1[0]
        
        if s1 == s2:
            return True

        return False

        


        

        
        
