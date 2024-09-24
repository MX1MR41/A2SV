class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.trie = TrieNode()

    def insert(self, num):
        root = self.trie

        for dig in num:
            if dig not in root.children:
                root.children[dig] = TrieNode()
            root = root.children[dig]

    def check(self, num):
        root = self.trie
        ans = 0
        for dig in num:
            if dig not in root.children:
                return ans
            root = root.children[dig]
            ans += 1

        return ans



class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # build a trie from the numbers of one of the arrays
        # check the trie with thenumbers of the other array
        trie = Trie()
        for num in arr1:
            trie.insert(str(num))

        ans = 0
        for num in arr2:
            ans = max(ans, trie.check(str(num)))

        return ans
        
