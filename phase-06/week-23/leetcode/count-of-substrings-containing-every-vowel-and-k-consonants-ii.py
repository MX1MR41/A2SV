class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        # sliding window
        # to find the number of subs with at least k consonants, we can compute
        # the number of subs with at least k + 1 consonants and also the 
        # number of subs with at least k consonants. 
        # Then f(k) - f(k + 1) would give us EXACTLY the number of subs with
        # exactly k consonants

        vowels = {'a', 'e', 'i', 'o', 'u'}

        def atleastk(k):
            vows = Counter()
            cs = 0
            l = 0
            res = 0
            for r in range(len(word)):
                right = word[r]

                if right in vowels:
                    vows[right] += 1
                else:
                    cs += 1

                while len(vows) == 5 and cs >= k:
                    res += (len(word) - r)

                    left = word[l]
                    if left in vowels:
                        vows[left] -= 1
                        if vows[left] == 0:
                            del vows[left]

                    else:
                        cs -= 1

                    l += 1

            return res


        return atleastk(k) - atleastk(k + 1)

