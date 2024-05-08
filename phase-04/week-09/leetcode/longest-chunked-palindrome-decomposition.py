class Solution:
    def longestDecomposition(self, text: str) -> int:
        # two pointers with greddy approach
        # traverse from left and right and every time we find the same word, count as 2

        l, r = 0, len(text) - 1
        left = right = ""
        res = 0

        while l < r:
            left += text[l]
            right += text[r]

            if left == right[::-1]:
                res += 2
                left = right = ""

            l += 1
            r -= 1
        
        # the text was not palindromic OR if the text was palindromic AND odd length
        if (l == r and len(left) == 0) or len(left):
            res += 1

        return res
