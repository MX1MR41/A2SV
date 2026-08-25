class TrieNode:
    def __init__(self):
        self.children = {}
        self.indices = set()

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word, index):
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()

            node = node.children[i]
            node.indices.add(index)

    def isPrefix(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                return set()

            node = node.children[i]

        return node.indices


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        # trie
        # Use two tries, one for the words as they are, another for the words reversed
        # the trie nodes store a set of the indices of the words that pass through that node's letter.
        # Iterate backwards on the words list; for every word, get the list of indices of words
        # it prefixes and the list of indices of words it suffixes.
        # The total would be the intersection of those two lists 
        # i.e. inidces of words it both prefixes and suffixes
        prefixTrie = Trie()
        suffixTrie = Trie()
        pairs = 0

        n = len(words)
        for i in range(n - 1, -1, -1):
            word = words[i]

            prefixFor = prefixTrie.isPrefix(word)
            suffixFor = suffixTrie.isPrefix(word[::-1])

            prefixAndSuffixFor = prefixFor.intersection(suffixFor)

            pairs += len(prefixAndSuffixFor)

            prefixTrie.add(word, i)
            suffixTrie.add(word[::-1], i)

        return pairs
        
