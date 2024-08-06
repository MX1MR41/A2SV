class Solution:
    def minimumPushes(self, word: str) -> int:
        # we start from the most frequent letters and
        # keep taking 8 letters at a time and assigning them
        # a minimum cost by multiplying with a multiplier that
        # increases every 8'th iteration

        cnt = Counter(word)
        letters = sorted(cnt.items(), key = lambda x: x[1])

        tot = 0
        multiplier = 1
        counter = 0
        while letters:
            letter, freq = letters.pop()
            tot += freq * multiplier
            counter += 1
            if counter == 8:
                counter = 0
                multiplier += 1

        return tot




        
