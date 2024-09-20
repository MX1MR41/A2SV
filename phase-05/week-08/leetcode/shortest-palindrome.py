class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s == s[::-1]:  # If s is already a palindrome, return it
            return s
        
        n = len(s)
        ans = 0  # Track the longest prefix palindrome
        
        for i in range(n):
            # Check if the substring from the start to index i forms a palindrome
            if s[:i+1] == s[:i+1][::-1]:
                ans = i + 1  # Update the longest palindrome length
        
        # We need to add the reverse of the suffix (part after the palindrome) to the front
        add = s[ans:][::-1]
        return add + s
