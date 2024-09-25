class TrieNode:
    def __init__(self):
        self.children = defaultdict(int)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root

        for letter in word:
            if letter not in root.children:
                root.children[letter] = TrieNode()
            root = root.children[letter]

            root.children["count"] += 1

    def check(self, word):
        root = self.root
        score = 0

        for letter in word:
            root = root.children[letter]
            score += root.children["count"]

        return score

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        # construct a trie from all the words
        # in addition to its children, the trieNode will have a variable to count frequency
        # calculate the score of each word by adding up all the freqs of all the prefixes
        trie = Trie()

        for word in words:
            trie.insert(word)

        ans = []
        for word in words:
            score = trie.check(word)
            ans.append(score)

        return ans
        
