class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        res = 0

        for i in words:
            j = set(i)

            for w in j:
                if w not in allowed:
                    break
            else:
                res += 1

        return res
        
