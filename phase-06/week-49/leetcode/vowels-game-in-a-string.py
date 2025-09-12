class Solution:
    def doesAliceWin(self, s: str) -> bool:
        #JusticeForBob

        vows = 0
        for i in s:
            if i in {'a', 'e', 'i', 'o', 'u'}:
                vows += 1

        if vows == 0:
            return False

        return True

        
