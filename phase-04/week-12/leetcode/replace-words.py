class TrieNode:
    def __init__(self):
        self.root = [None] * 26
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        dummy = self.root

        for i in word:
            ind = ord(i) - 97
            if dummy.root[ind] is None:
                new = TrieNode()
                dummy.root[ind] = new
            dummy = dummy.root[ind]

        dummy.end = True

    def search(self, word):
        dummy = self.root
        ind = ord(word[0]) - 97
        if dummy.root[ind] is None: return ""
        root_word = ""

        for i in word:
            ind = ord(i) - 97
            if dummy.end: return root_word
            if dummy.root[ind] is None: 
                if not any([i for i in dummy.root]):
                    return root_word
                else: return ""

            dummy = dummy.root[ind]

            root_word += i

        return root_word if dummy.end else ""





class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        prefix = Trie()
        sentence = sentence.split(" ")
        for word in dictionary:
            prefix.insert(word)


        for i in range(len(sentence)):
            word = sentence[i]
            root = prefix.search(word)
            if not root: continue
            sentence[i] = root

        return " ".join(sentence)

        
