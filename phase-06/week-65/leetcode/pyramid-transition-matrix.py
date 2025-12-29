class TrieNode:
    def __init__(self):
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root

        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()

            node = node.children[i]

    def search(self, word):
        node = self.root

        for i in word:
            if i not in node.children:
                return []

            node = node.children[i]

        return list(node.children.keys())

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # backtracking + trie
        # use trie to efficiently find what the next set of possible letters could be
        # given the base blocks
        # build the pyramid initially with empty cells except for the bottom level
        # then move block by block in an upwards and leftwards manner trying to fill 
        # the blocks with valid options
        trie = Trie()

        for pat in allowed:
            trie.add(pat)

        n = len(bottom)

        pyramid = [["" for _ in range(i)] for i in range(n)]
        pyramid.append(list(bottom))

        def dfs(level, ind):
            if level == 0:
                return True


            base = pyramid[level + 1][ind] + pyramid[level + 1][ind + 1]
            options = trie.search(base)

            for opt in options:
                pyramid[level][ind] = opt

                next_ind = ind + 1
                if next_ind == level:
                    next_ind = 0
                    next_level = level - 1
                else:
                    next_level = level

                if dfs(next_level, next_ind):
                    return True


            return False

        return dfs(n - 1, 0)





        
