class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = Counter(s1.strip().split())
        for w in s2.strip().split():
            words[w] += 1

        return [i for i in words if words[i] == 1]

        
