class Solution:
    def numberOfSpecialChars(self, word: str) -> int:

        n = len(word)
        last_lower = [n] * 26
        first_upper = [n] * 26

        for i in range(n):
            lett = word[i]
            if lett.islower():
                last_lower[ord(lett) - ord('a')] = i

            else:
                first_upper[ord(lett) - ord('A')] = min(first_upper[ord(lett) - ord('A')], i)

        return sum(1 for i in range(26) if (last_lower[i] < first_upper[i] and first_upper[i] < n))



        
