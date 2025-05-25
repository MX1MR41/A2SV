class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        
        res = 0
        unique = False

        seen = defaultdict(int)

        for w in words:
            rev = w[::-1]
            if seen[rev]:
                res += 4
                seen[rev] -= 1

            else:
                seen[w] += 1

        for w in seen:
            if seen[w] >= 1 and w == w[::-1]:
                res += 2
                break
                


        return res

        
