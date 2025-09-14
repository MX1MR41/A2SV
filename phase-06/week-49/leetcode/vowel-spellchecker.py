class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.indices = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word, index):
        node = self.root

        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()

            node = node.children[i]
            if not node.indices:
                node.indices.append(index)

        node.end = True

    def search(self, word):
        node = self.root

        for i in word:
            if i not in node.children:
                return None

            node = node.children[i]

        if not node.end:
            return None

        return node.indices[0]




class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        # Trie
        # use three tries to maintain the order of precedence
        # keep track of the earliest index seen so far for every TrieNode
        exact = Trie()
        case_insensitive = Trie()
        devoweled = Trie()

        vows = {'a', 'e', 'i', 'o', 'u'}

        for index, word in enumerate(wordlist):
            exact.add(word, index)
            case_insensitive.add(word.lower(), index)

            de_word = ""
            for i in word.lower():
                if i in vows:
                    de_word += "*"
                else:
                    de_word += i 

            devoweled.add(de_word, index)

        res = []

        for word in queries:
            index = exact.search(word)
            if index is not None:
                res.append(wordlist[index])
                continue

            index = case_insensitive.search(word.lower())
            if index is not None:
                res.append(wordlist[index])
                continue

            de_word = ""
            for i in word.lower():
                if i in vows:
                    de_word += "*"
                else:
                    de_word += i

            index = devoweled.search(de_word)
            if index is not None:
                res.append(wordlist[index])
                continue

            res.append("")

        return res

