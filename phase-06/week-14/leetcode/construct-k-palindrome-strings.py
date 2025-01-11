class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # we can space out the odd frequency letters to separate palindromes
        # and we can space the even frequency letters any way we want
        
        if k == len(s):
            return True

        if k > len(s):
            return False

        count = Counter(s)

        odds = 0
        for i, j in count.items():
            if j % 2:
                odds += 1

        if odds > k:
            return False

        return True
        
