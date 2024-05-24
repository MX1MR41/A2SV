class TrieNode:
    def __init__(self):
        self.root = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for i in word:
            if i not in curr.root:
                curr.root[i] = TrieNode()
            curr = curr.root[i]
        curr.end = True

    def search(self, word: str) -> bool:
        def dfs(node, word):
            if not word:
                return node.end
            if word[0] == '.':
                for nxt in node.root:
                    if dfs(node.root[nxt], word[1:]):
                        return True
            elif word[0] in node.root:
                return dfs(node.root[word[0]], word[1:])
            return False
        return dfs(self.root, word)

class WordDictionary:
    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        self.root.insert(word)

    def search(self, word: str) -> bool:
        return self.root.search(word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
