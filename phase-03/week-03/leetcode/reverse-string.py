class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def rev(a, b):
            if a >= b:
                return
            s[a], s[b] = s[b], s[a]
            rev(a+1, b-1)

        rev(0, len(s)-1)
