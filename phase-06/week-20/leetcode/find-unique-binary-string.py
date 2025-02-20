class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.trie = TrieNode()

    def add(self, s):
        curr = self.trie
        
        for i in s:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]


    def present(self, s):
        curr = self.trie

        for i in s:
            if i not in curr.children:
                return False

            curr = curr.children

        return True

    
        
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # backtracking + trie
        # use a trie to keep track o the original strings that we are given
        # our backtracking function will have the current trie node we are exploring
        # if either character is not in ou current node, we greedily use it
        
        trie = Trie()
        have = set(nums)
        for num in nums:
            trie.add(num)

        n = len(nums)

        res = None
        def dfs(s, node):
            nonlocal res
            if len(s) == n:
                if s not in have:
                    res = s
                    return True

                return 

            
            if "1" not in node.children:
                temp = dfs(s + "1", node)
                if temp:
                    return True

            if "0" not in node.children:
                temp = dfs(s + "0", node)
                if temp:
                    return True

            return dfs(s + "1", node.children["1"]) or dfs(s + "0", node.children["0"])


        dfs("", trie.trie)

        return res
            

        
