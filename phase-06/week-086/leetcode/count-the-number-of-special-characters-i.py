class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        return len([i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if i in word and i.lower() in word])
        