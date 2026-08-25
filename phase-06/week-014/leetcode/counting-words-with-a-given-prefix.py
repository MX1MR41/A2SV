class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        n = len(words)
        m = len(pref)
        for word in words:
            count += word[:m] == pref

        return count
        
