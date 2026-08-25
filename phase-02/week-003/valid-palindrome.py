class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        pal = ""
        for i in s:
            o = ord(i)
# ascii values: 0 - 9                    A - Z                    a - z
            if (o >= 48 and o <= 57) or (o >= 65 and o <= 90) or (o >= 97 and o <= 122):
                pal += i

        if not pal: # if empty
            return True

        pal = pal.lower()
        i , j = 0, len(pal) - 1
        while i < j:
            if pal[i] != pal[j]:
                return False

            i += 1
            j -= 1

        return True