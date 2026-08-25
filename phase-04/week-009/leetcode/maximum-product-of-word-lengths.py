class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # bit manipulation coupled with dynamic programming
        # represent the words as a bitmask where the ith bit(from the left) is 1 if
        # the ith letter in the alphabet exists in the word
        # to check if the letters in two words are unique, we AND them and the result must be 0

        # stores the bitmask of a word once calculated so as not to recalculate it
        masked = defaultdict(int)
        # converts a string into a bitmask representation
        def mask(word):
            ans = 0
            for i in word:
                ans |= 1 << (ord(i) - 96)

            return ans

        res = 0

        for i in words:
            for j in words: 
                if i == j: continue

                maski = mask(i) if not masked[i] else masked[i]
                masked[i] = maski
                maskj = mask(j) if not masked[j] else masked[j]
                masked[j] = maskj

                curr = maski & maskj

                if not str(bin(curr))[2:].count("1"): # all letters are unique
                    res = max(res, len(i)*len(j))


        return res
        
