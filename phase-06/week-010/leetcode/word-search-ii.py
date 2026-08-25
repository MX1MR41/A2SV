class TrieNode:
    def __init__(self):
        self.children = dict()
        self.end = False

class Trie:
    def __init__(self):
        self.trie = TrieNode()

    def add(self, word):
        curr = self.trie
        for i in word:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]

        curr.end = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # trie + backtracking
        # the brute force approach would be to do a bfs search over the board to find words
        # instead we can use a trie as a dictionary of the words given, then when traversing
        # through the board we move into a next cell only if it represents a valid next letter
        # i.e. it exists in the children of our current trie node

        trie = Trie()
        for word in words:
            trie.add(word)


        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(board), len(board[0])

        inbound = lambda i, j: 0 <= i < m and 0 <= j < n
        ans = set()

        def find(i, j, node, word, seen):
            nonlocal ans

            # a full valid word found because this trie node is a possible end
            if node.end:
                ans.add(word)
            
            # we have run out of possible next letters
            if not node.children:
                return 

            # keep track of visited cells to avoid revisiting
            seen.add((i, j))


            for di, dj in dirs:
                ni, nj = i + di, j + dj
                # if this cell is valid and contains a possible next letter to build our word
                if inbound(ni, nj) and (ni, nj) not in seen and board[ni][nj] in node.children:
                    letter = board[ni][nj]
                    # move into that cell along with the next trie node with a copy of our visited set
                    find(ni, nj, node.children[letter], word + letter, seen.copy())


        for i in range(m):
            for j in range(n):
                letter = board[i][j]

                # if it is a possible start letter
                if letter in trie.trie.children:
                    find(i, j, trie.trie.children[letter], letter, set())
  
        return list(ans)
