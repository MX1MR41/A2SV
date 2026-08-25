class TrieNode:
    def __init__(self):
        self.root = dict()
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
        curr = self.root
        for i in word:
            if i not in curr.root: return False

            curr = curr.root[i]

        return curr.end
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in prefix:
            if i not in curr.root: return False

            curr = curr.root[i]

        return True
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
