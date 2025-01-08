class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1, str2):
            m, n = len(str1), len(str2)
            return str1 == str2[:m] and str1 == str2[-m:]

        pairs = 0
        n = len(words)
        for i in range(n):
            a = words[i]
            for j in range(i + 1, n):
                b = words[j]
                if isPrefixAndSuffix(a, b):
                    pairs += 1


        return pairs
        
