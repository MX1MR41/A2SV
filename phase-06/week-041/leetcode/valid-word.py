class Solution:
    def isValid(self, word: str) -> bool:
        vowels = set()
        for i in ["a", "e", "i", "o", "u"]:
            vowels.add(i)
            vowels.add(i.upper())

        consonants = set()
        for i in [
            "b",
            "c",
            "d",
            "f",
            "g",
            "h",
            "j",
            "k",
            "l",
            "m",
            "n",
            "p",
            "q",
            "r",
            "s",
            "t",
            "v",
            "w",
            "x",
            "y",
            "z",
        ]:
            consonants.add(i)
            consonants.add(i.upper())

        nums = set([str(i) for i in range(10)])

        if len(word) < 3:

            return False

        for i in word:
            if i in vowels:
                break
        else:

            return False

        for i in word:
            if i in consonants:
                break
        else:

            return False

        for i in word:
            if i not in nums and i not in vowels and i not in consonants:

                return False

        return True
