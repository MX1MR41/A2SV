class Solution:
    def __init__(self):
        self.letters = [0]

        while len(self.letters) < 500:
            prev = self.letters[:]
            for p in prev:
                p = (p + 1) % 26
                self.letters.append(p)

    def kthCharacter(self, k: int) -> str: 

        return chr(self.letters[k-1] + 97)
