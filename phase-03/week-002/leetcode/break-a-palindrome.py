class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        s = list(palindrome)
        n = len(s)

        if n <= 1:
            return ""


        for i in range(n):
            if n % 2 and i == ceil(n/2) - 1: # pass if it is the middle element
                continue

            j = s[i] 
            if ord(j) > ord('a'):
                s[i] = 'a'
                return "".join(s)
        else:
            s[-1] = 'b'
            return "".join(s)
