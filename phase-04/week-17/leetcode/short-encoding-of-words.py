class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word):
        dummy = self.trie
        for w in word:
            if w not in dummy.children:
                dummy.children[w] = TrieNode()

            dummy = dummy.children[w]

        dummy.end = True




class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        # use trie where the words are reversed so that we can overlap 
        # words which have common suffixes
        trie = Trie()
        for word in words:
            trie.insert(word[::-1])

        res = 0

        def dfs(node, path):
            nonlocal res

            if not node.children:
                # + 1 to account for the # symbol at the end of every word
                res += path + 1
                return

            for c in node.children:
                dfs(node.children[c], path + 1)

                
        trie = trie.trie
        for c in trie.children:
            
            dfs(trie.children[c], 1)

        return res
        
