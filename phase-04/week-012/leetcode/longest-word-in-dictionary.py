class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        dummy = self.root
        for i in word:
            if i not in dummy.children:
                dummy.children[i] = TrieNode()
            dummy = dummy.children[i]
        dummy.end = True

    def check_prefix(self, word):
        dummy = self.root
        for i in word:
            if i not in dummy.children or not dummy.children[i].end:
                return False
            dummy = dummy.children[i]
        return True

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()  
        ans = ""
        trie = Trie()
        trie.insert("")  
        
        for word in words:
            if trie.check_prefix(word[:-1]):
                trie.insert(word)
                if len(word) > len(ans) or (len(word) == len(ans) and word < ans):
                    ans = word
        
        return ans


