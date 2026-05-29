class TrieNode:
    def __init__(self):
        self.children = {}
        self.heap = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word, ind):
        n = len(word)
        node = self.root

        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()

            node = node.children[w]

            heappush(node.heap, (n, ind))

        
    def check(self, word):
        node = self.root
        res = -1

        for w in word:
            if w not in node.children:
                break

            node = node.children[w]
            res = node.heap[0][1]

        return res





class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        # trie + heap

        trie = Trie()
        fallback = [float("inf"), float("inf")]

        for ind, word in enumerate(wordsContainer):
            trie.add(word[::-1], ind)
            if len(word) < fallback[0]:
                fallback = [len(word), ind]


        res = []
        for word in wordsQuery:
            curr = trie.check(word[::-1])
            if curr == -1:
                curr = fallback[1]

            res.append(curr)
        
        return res
        
