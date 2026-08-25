class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0   
        n1, n2 = len(name), len(typed)
        while i <= n1 and j < n2:
            if i < n1 and typed[j] == name[i]:
                j += 1
                i += 1
            elif typed[j] == name[i-1] and i != 0:
                j += 1
            else:
                return False        
        return i == n1 and j == n2
        