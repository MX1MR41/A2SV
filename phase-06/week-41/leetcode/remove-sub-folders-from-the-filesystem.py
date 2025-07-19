class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {}

class Trie:
    def __init__(self):
        self.trie = TrieNode()
        self.folders = []

    def add(self, folder):
        folder = folder.split("/")[1:]

        curr = ""

        node = self.trie

        for f in folder:
            if f not in node.children:
                node.children[f] = TrieNode()

            node = node.children[f]

            curr += "/" + f

            if node.end:
                return

        node.end = True
        
        self.folders.append(curr)



class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:

        folder.sort()

        trie = Trie()

        for f in folder:
            trie.add(f)

        return trie.folders


        
        
