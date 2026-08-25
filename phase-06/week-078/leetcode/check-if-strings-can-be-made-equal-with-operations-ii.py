class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        return (
            sorted([s1[i] for i in range(0, len(s1), 2)]) == sorted([s2[i] for i in range(0, len(s2), 2)])
            and
            sorted([s1[i] for i in range(1, len(s1), 2)]) == sorted([s2[i] for i in range(1, len(s2), 2)])


        )
        
